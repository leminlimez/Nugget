"""MobileGestalt transport for the foreground NuggetQuery iOS companion.

Only the companion runs worse_query. No sandbox token is usable on the host.
Other tweaks continue to use the existing restore transport.
"""
import asyncio
import plistlib
from pathlib import Path
from uuid import uuid4

from PySide6.QtCore import QCoreApplication
from pymobiledevice3.services.house_arrest import HouseArrestService
from pymobiledevice3.services.installation_proxy import InstallationProxyService

from src.exceptions.nugget_exception import NuggetException
from src.tweaks.basic_plist_locations import FileLocation

MGA_DOMAIN = "SysSharedContainerDomain-systemgroup.com.apple.mobilegestaltcache"
MGA_RELATIVE_PATH = "Library/Caches/com.apple.MobileGestalt.plist"
PENDING = "/Documents/NuggetQuery-pending.plist"
RESULT = "/Documents/NuggetQuery-result.plist"
PROCESSING = "/Documents/NuggetQuery-processing.plist"


def split_query_files(files):
    """Reject unsupported raw paths before either transport changes the device."""
    query, regular = [], []
    for file in files:
        if ((file.domain == MGA_DOMAIN and file.restore_path.lstrip("/") == MGA_RELATIVE_PATH)
                or (not file.domain and file.restore_path == FileLocation.mga.value)):
            query.append(file)
        elif not file.domain:
            raise NuggetException(f"worse_query does not support this path: {file.restore_path}")
        elif file.domain in ("SystemPreferencesDomain", "DatabaseDomain") and (
            file.restore_path.lstrip("/").startswith(("FeatureFlags/", "eligibilityd/", "os_eligibility/"))
        ):
            raise NuggetException(f"worse_query does not support this path: {file.restore_path}")
        else:
            regular.append(file)
    if len(query) > 1:
        raise NuggetException("Duplicate MobileGestalt operations in one request.")
    return query, regular


def make_request(file, build, version):
    contents = Path(file.contents_path).read_bytes() if file.contents_path else file.contents
    if not isinstance(contents, bytes):
        raise NuggetException("Invalid MobileGestalt contents.")
    if contents:
        try:
            if not isinstance(plistlib.loads(contents).get("CacheExtra"), dict):
                raise ValueError("CacheExtra is missing")
        except (AttributeError, ValueError, plistlib.InvalidFileException) as exc:
            raise NuggetException("Invalid MobileGestalt plist.") from exc
    return {
        "protocol": 1, "id": str(uuid4()), "build": build, "version": version,
        "operation": "write" if contents else "restore_original", "contents": contents,
    }


async def perform_worse_query(file, device, lockdown_client, progress_callback, timeout=180):
    request = make_request(file, device.build, device.version)
    async with InstallationProxyService(lockdown_client) as ips:
        apps = await ips.get_apps(application_type="User", calculate_sizes=False)
    companions = [app["CFBundleIdentifier"] for app in apps.values()
                  if app.get("CFBundleExecutable") == "NuggetQuery"]
    if len(companions) != 1:
        raise NuggetException(QCoreApplication.tr(
            "Install one signed NuggetQuery companion app with an App Group to use MobileGestalt on iOS 27.0–27.2."
        ), detailed_text="See companion/README.md in the Nugget source repository.")

    async with HouseArrestService(lockdown=lockdown_client, bundle_id=companions[0], documents_only=True) as afc:
        if await afc.exists(PENDING) or await afc.exists(PROCESSING):
            raise NuggetException(QCoreApplication.tr(
                "A NuggetQuery request is already pending. Complete or discard it in the companion app first."
            ))
        # Publish a complete plist; the companion never sees a partial upload.
        staging = PENDING + "." + request["id"]
        try:
            await afc.set_file_contents(staging, plistlib.dumps(request, fmt=plistlib.FMT_BINARY))
            await afc.rename(staging, PENDING)
        finally:
            if await afc.exists(staging):
                await afc.rm(staging)
        progress_callback(QCoreApplication.tr(
            "Open NuggetQuery on your device, load the pending request, then tap Apply. Keep it open."
        ))
        deadline = asyncio.get_running_loop().time() + timeout
        while asyncio.get_running_loop().time() < deadline:
            if await afc.exists(RESULT):
                result = plistlib.loads(await afc.get_file_contents(RESULT))
                if result.get("id") == request["id"]:
                    if result.get("protocol") != 1 or result.get("build") != device.build:
                        raise NuggetException("NuggetQuery returned an incompatible result.")
                    if result.get("success") is not True:
                        raise NuggetException("NuggetQuery: " + str(result.get("message", "Write failed.")))
                    # Do not reboot the device before the app has cleared its claim.
                    if not await afc.exists(PROCESSING):
                        return
            await asyncio.sleep(1)
        # Leave the pending request visible: deleting it could race an active write.
        raise NuggetException(QCoreApplication.tr(
            "Timed out waiting for NuggetQuery. The write result is unknown. Check the companion app before retrying."
        ))
