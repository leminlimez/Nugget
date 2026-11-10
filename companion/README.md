# NuggetQuery (experimental)

Device-side MobileGestalt bridge for **iOS/iPadOS 27.0–27.2 inclusive**. Other
Nugget features keep their existing restore transport and limitations. This
does **not** enable BookRestore, Feature Flags, AI eligibility, passcode themes
or resolution/RDAR modifications on iOS 27. The home screen labels this support
experimental until real-device validation is available.

## Build and install

1. On a Mac with Xcode 27 or newer, open `NuggetQuery.xcodeproj`.
2. Select the NuggetQuery target, set your development team and a unique bundle
   identifier. Keep the target/product executable named **NuggetQuery** so the
   desktop can discover it even if the bundle ID changes.
3. Set the `NUGGET_QUERY_APP_GROUP` build setting to a new, dedicated App Group
   registered to your team. The upstream PoC replaces this group's `Library/Caches`
   while acquiring access. Add that same group under Signing & Capabilities → App Groups.
   The build setting is used by both the entitlements and the generated
   `NuggetQueryAppGroup` Info.plist key. Ensure your provisioning profile includes it.
4. Build and run on the device. Keep File Sharing enabled (configured in the
   project). This exploit needs a real device; a simulator cannot validate it.

The Linux development environment cannot compile/sign this project. No prebuilt
or signed IPA is included. App Group provisioning must work before this bridge
can run.

## Apply and reset

1. In NuggetQuery, tap **Export current MobileGestalt**, then share the exported
   plist to your computer. Alternatively copy it from the app's Documents folder
   through Finder/Apple Devices File Sharing. Select it on Nugget's Apply page.
2. Select MobileGestalt tweaks and click Apply in Nugget.
3. Open NuggetQuery, tap **Load pending request**, review the operation/build,
   then tap **Apply to this device** within three minutes. Keep the app open.
4. Nugget waits for the matching result. It reports success only after the app
   writes and reads the exact bytes back. Restart to see changes. If a selection
   also uses regular restore domains, those are restored after the companion
   succeeds; a later restore failure does not undo the MobileGestalt write.
5. **Reset → Mobile Gestalt** uses the same flow with `restore_original`. It
   restores the file saved before the first write for the current OS build.
   Reset fails if that backup is missing. A file modified before the first
   NuggetQuery write becomes the baseline; this does not reconstruct factory data.

Keep `MobileGestalt-original-<build>.plist` in the companion's Documents folder.
It is a plist wrapper with `build` and `contents` fields, not a direct
MobileGestalt export. Deleting the app deletes its backups. Backups from another
OS build are never used for reset.

On timeout/disconnection the write status is **unknown**. Check the app and
current file before retrying; finish or discard the pending/interrupted request
in the companion. The desktop does not delete an in-flight request. Requests
are not executed automatically and do not accept arbitrary destination paths.
If the sandbox token or filesystem permissions deny access, the app returns
the error; the desktop does not fall back to BookRestore. The bridge preserves
the existing file's inode and ownership. It attempts to restore the immediately
previous contents if writing or verification fails; a process/device crash can
still interrupt a write. The saved original remains available separately.

## Protocol

House Arrest vends the signed companion's Documents directory. The host uploads
a complete binary plist to a temporary file, then renames it to
`NuggetQuery-pending.plist`. Version 1 requests contain `protocol`, a UUID `id`,
`build`, `version`, `operation` (`write` or `restore_original`) and `contents`
(plist data, empty for reset). The app checks its own OS version/build, claims
the request as `NuggetQuery-processing.plist`, and publishes
`NuggetQuery-result.plist` atomically with `protocol`, `id`, `build`, `success`
and `message`. Old result UUIDs are ignored. Pending/processing markers prevent
overwriting unfinished requests.

## Upstream and license

`NuggetQuery/worse_query.m` and `.h` are unmodified copies from
[forcequitOS/worse_query](https://github.com/forcequitOS/worse_query), commit
`d1540e20cd82b974d891e0551ced6d6aeb570ac2`. Copyright 2026 Taj C (forcequit),
GPL-3.0-or-later; see `LICENSE.worse_query`. The Xcode project is adapted from
that repository; the bridge/UI are additions for Nugget.

The upstream README says “iOS 26.0–26.7.2 / 27.2” and lists SystemGroup access
for iOS 27. This bridge restricts the requested integration to 27.0–27.2 and to
the MobileGestalt SystemGroup container. Version recognition and transport tests
are not proof that any particular tweak works on all devices/builds. Confirm
export, write/read-back, reboot behavior and original-backup reset on each target
OS before calling this stable support.

Host checks: `QT_QPA_PLATFORM=offscreen .env/bin/python -m unittest discover -s tests -v`.
