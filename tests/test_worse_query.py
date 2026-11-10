import plistlib
import unittest
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

# Match the application's initialization order (its existing GUI modules have
# circular imports if DeviceManager is imported first).
import src.gui.main_window
from src.devicemanagement.constants import Device
from src.devicemanagement.device_manager import DeviceManager
from src.exceptions.nugget_exception import NuggetException
from src.gui.pages.pages_list import Page, get_resettable_pages
from src.restore import worse_query as query
from src.restore.bookrestore import BookRestoreApplyMethod, BookRestoreFileTransferMethod
from src.restore.restore import FileToRestore
from src.tweaks.basic_plist_locations import FileLocation


def device(version="27.1", build="24B123"):
    return Device("test-udid", True, "Test", version, build, "iPhone18,3", "test",
                  "test", "en_US", "")


def mga(contents=None, domain="", path=None):
    return FileToRestore(
        contents=plistlib.dumps({"CacheExtra": {"example": True}}) if contents is None else contents,
        restore_path=path or FileLocation.mga.value, domain=domain,
    )


class VersionTests(unittest.TestCase):
    def test_requested_range_and_unchanged_restore_capabilities(self):
        for version in ("27", "27.0", "27.0.0", "27.0.1", "27.1", "27.1.2", "27.2"):
            with self.subTest(version=version):
                dev = device(version)
                self.assertTrue(dev.supported())
                self.assertTrue(dev.has_worse_query())
                self.assertTrue(dev.supports_mobilegestalt())
                self.assertFalse(dev.has_bookrestore())
                self.assertFalse(dev.has_partial_sparserestore())
                self.assertTrue(dev.is_exploit_fully_patched())

    def test_boundaries_and_legacy_support(self):
        for version, supported, gestalt in (("16.9", False, True), ("17.0", True, True),
                ("18.1", True, True), ("26.1", True, True), ("26.2", True, False),
                ("26.9", True, False), ("26.10", False, False),
                ("27.2.1", False, False), ("27.3", False, False), ("28.0", False, False)):
            with self.subTest(version=version):
                dev = device(version)
                self.assertEqual(dev.supported(), supported)
                self.assertFalse(dev.has_worse_query())
                self.assertEqual(dev.supports_mobilegestalt(), gestalt)


class PlanTests(unittest.TestCase):
    def test_split_mga_from_regular_files(self):
        native = mga(domain=query.MGA_DOMAIN, path=query.MGA_RELATIVE_PATH)
        regular = FileToRestore(b"test", "Library/test", domain="HomeDomain")
        self.assertEqual(query.split_query_files([native, regular]), ([native], [regular]))

    def test_unsupported_paths_rejected_before_transport(self):
        for domain, path in (("", "/var/mobile/Library/Caches/TelephonyUI-10/key.png"),
                ("", FileLocation.resolution.value),
                ("SystemPreferencesDomain", "/FeatureFlags/Global.plist"),
                ("DatabaseDomain", "eligibilityd/eligibility.plist"),
                ("DatabaseDomain", "os_eligibility/eligibility.plist")):
            with self.subTest(path=path), self.assertRaises(NuggetException):
                query.split_query_files([mga(), FileToRestore(b"test", path, domain=domain)])

    def test_duplicate_mga_rejected(self):
        with self.assertRaises(NuggetException):
            query.split_query_files([mga(), mga()])

    def test_payload_contains_no_caller_controlled_destination(self):
        request = query.make_request(mga(), "24B123", "27.1")
        self.assertEqual(request["operation"], "write")
        self.assertEqual(request["build"], "24B123")
        self.assertNotIn("path", request)
        self.assertEqual(plistlib.loads(plistlib.dumps(request)), request)

    def test_reset_is_original_restore_not_empty_write(self):
        self.assertEqual(query.make_request(mga(b""), "build", "27.0")["operation"], "restore_original")

    def test_invalid_gestalt_is_rejected(self):
        for contents in (b"not a plist", plistlib.dumps({}), plistlib.dumps([]), "text", None):
            with self.subTest(contents=contents), self.assertRaises(NuggetException):
                file = mga()
                file.contents = contents
                query.make_request(file, "build", "27.0")

    def test_contents_path(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "mga.plist"
            path.write_bytes(mga().contents)
            file = mga()
            file.contents = None
            file.contents_path = str(path)
            self.assertEqual(query.make_request(file, "build", "27.0")["contents"], path.read_bytes())


class FakeAFC:
    def __init__(self, outcome=True):
        self.files = {}
        self.outcome = outcome
        self.published = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return False

    async def exists(self, path):
        return path in self.files

    async def set_file_contents(self, path, data):
        self.files[path] = data

    async def rename(self, source, target):
        self.files[target] = self.files.pop(source)
        self.published = plistlib.loads(self.files[target])
        if self.outcome is not None:
            result = {"protocol": 1, "id": self.published["id"], "build": self.published["build"],
                      "success": bool(self.outcome), "message": "permission denied"}
            if callable(self.outcome):
                self.outcome(result)
            self.files[query.RESULT] = plistlib.dumps(result)

    async def get_file_contents(self, path):
        return self.files[path]

    async def rm(self, path):
        del self.files[path]


@contextmanager
def transport(afc, apps=None):
    ips = SimpleNamespace(get_apps=AsyncMock(return_value=apps if apps is not None else {
        "custom.id": {"CFBundleIdentifier": "custom.id", "CFBundleExecutable": "NuggetQuery"}
    }))
    context = AsyncMock()
    context.__aenter__.return_value = ips
    with patch.object(query, "InstallationProxyService", return_value=context), \
            patch.object(query, "HouseArrestService", return_value=afc) as arrest:
        yield arrest


class TransportTests(unittest.IsolatedAsyncioTestCase):
    async def test_signed_custom_bundle_id_and_verified_success(self):
        afc = FakeAFC()
        with transport(afc) as arrest:
            await query.perform_worse_query(mga(), device(), None, lambda _: None)
        self.assertEqual(arrest.call_args.kwargs["bundle_id"], "custom.id")
        self.assertEqual(list(afc.files), [query.PENDING, query.RESULT])
        self.assertEqual(afc.published["operation"], "write")

    async def test_device_error_propagates(self):
        with transport(FakeAFC(False)), self.assertRaisesRegex(NuggetException, "permission denied"):
            await query.perform_worse_query(mga(), device(), None, lambda _: None)

    async def test_absent_or_ambiguous_companion_rejected(self):
        for apps in ({}, {"a": {"CFBundleIdentifier": "a", "CFBundleExecutable": "NuggetQuery"},
                          "b": {"CFBundleIdentifier": "b", "CFBundleExecutable": "NuggetQuery"}}):
            with transport(FakeAFC(), apps), self.assertRaisesRegex(NuggetException, "Install one"):
                await query.perform_worse_query(mga(), device(), None, lambda _: None)

    async def test_pending_and_interrupted_requests_not_overwritten(self):
        for marker in (query.PENDING, query.PROCESSING):
            afc = FakeAFC()
            afc.files[marker] = b"existing request"
            with transport(afc), self.assertRaisesRegex(NuggetException, "already pending"):
                await query.perform_worse_query(mga(), device(), None, lambda _: None)
            self.assertIsNone(afc.published)

    async def test_stale_result_ignored_and_timeout_keeps_pending(self):
        afc = FakeAFC(lambda result: result.update(id="previous request"))
        with transport(afc), patch.object(query.asyncio, "sleep", new=AsyncMock()), \
                self.assertRaisesRegex(NuggetException, "unknown"):
            await query.perform_worse_query(mga(), device(), None, lambda _: None, timeout=0.001)
        self.assertIn(query.PENDING, afc.files)

    async def test_wrong_build_or_protocol_cannot_report_success(self):
        for changes in ({"build": "other-build"}, {"protocol": 2}):
            afc = FakeAFC(lambda result: result.update(changes))
            with transport(afc), self.assertRaisesRegex(NuggetException, "incompatible"):
                await query.perform_worse_query(mga(), device(), None, lambda _: None)

    async def test_verified_result_waits_for_processing_cleanup(self):
        class ClaimedAFC(FakeAFC):
            async def rename(self, source, target):
                await super().rename(source, target)
                self.files[query.PROCESSING] = b"claimed"
        afc = ClaimedAFC()
        with transport(afc), patch.object(query.asyncio, "sleep", new=AsyncMock()), \
                self.assertRaisesRegex(NuggetException, "unknown"):
            await query.perform_worse_query(mga(), device(), None, lambda _: None, timeout=0.001)


class RoutingTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.manager = DeviceManager.__new__(DeviceManager)
        self.manager.data_singleton = SimpleNamespace(current_device=device())
        self.manager.pref_manager = SimpleNamespace(auto_reboot=False, bookrestore_apply_mode=BookRestoreApplyMethod.AFC)

    async def test_native_only_never_calls_patched_restore_services(self):
        with patch("src.devicemanagement.device_manager.create_using_usbmux", new=AsyncMock(return_value=FakeAFC())), \
                patch("src.devicemanagement.device_manager.perform_worse_query", new=AsyncMock()) as native, \
                patch("src.devicemanagement.device_manager.perform_bookrestore", new=AsyncMock()) as book, \
                patch("src.devicemanagement.device_manager.restore_files", new=AsyncMock()) as restore:
            await self.manager.start_restore([mga()], True)
        native.assert_awaited_once()
        book.assert_not_awaited()
        restore.assert_not_awaited()

    async def test_invalid_mixed_selection_rejected_before_native_write(self):
        with patch("src.devicemanagement.device_manager.create_using_usbmux", new=AsyncMock(return_value=FakeAFC())), \
                patch("src.devicemanagement.device_manager.perform_worse_query", new=AsyncMock()) as native, \
                self.assertRaises(NuggetException):
            await self.manager.start_restore([mga(), FileToRestore(b"", "/var/db/eligibilityd/eligibility.plist")], True)
        native.assert_not_awaited()

    async def test_native_failure_prevents_regular_restore(self):
        with patch("src.devicemanagement.device_manager.create_using_usbmux", new=AsyncMock(return_value=FakeAFC())), \
                patch("src.devicemanagement.device_manager.perform_worse_query", new=AsyncMock(side_effect=NuggetException("failed"))), \
                patch("src.devicemanagement.device_manager.restore_files", new=AsyncMock()) as restore, \
                self.assertRaises(NuggetException):
            await self.manager.start_restore([mga(), FileToRestore(b"test", "Library/test", domain="HomeDomain")], True)
        restore.assert_not_awaited()

    async def test_legacy_bookrestore_still_uses_original_transport(self):
        self.manager.data_singleton.current_device = device("26.1")
        self.manager.pref_manager.bookrestore_transfer_mode = BookRestoreFileTransferMethod.LocalHost
        with patch("src.devicemanagement.device_manager.create_using_usbmux", new=AsyncMock(return_value=FakeAFC())), \
                patch("src.devicemanagement.device_manager.perform_worse_query", new=AsyncMock()) as native, \
                patch("src.devicemanagement.device_manager.perform_bookrestore", new=AsyncMock()) as book:
            await self.manager.start_restore([mga()], True)
        native.assert_not_awaited()
        book.assert_awaited_once()

    async def test_out_of_range_device_is_rejected_before_connecting(self):
        self.manager.data_singleton.current_device = device("27.2.1")
        with patch("src.devicemanagement.device_manager.create_using_usbmux", new=AsyncMock()) as connect, \
                self.assertRaisesRegex(NuggetException, "not supported"):
            await self.manager.start_restore([mga()], True)
        connect.assert_not_awaited()

    def test_reset_list_and_native_path_routing(self):
        pages = get_resettable_pages(self.manager)
        self.assertIn(Page.Gestalt, pages)
        self.assertNotIn(Page.FeatureFlags, pages)
        self.assertEqual(self.manager.get_domain_for_path(FileLocation.mga.value), (FileLocation.mga.value, ""))
        self.assertEqual(self.manager.get_domain_for_path(FileLocation.springboard.value),
                         ("mobile/com.apple.springboard.plist", "ManagedPreferencesDomain"))


if __name__ == "__main__":
    unittest.main()
