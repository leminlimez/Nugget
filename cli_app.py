from Sparserestore.restore import restore_files, FileToRestore, restore_file
from tweaks.tweaks import tweaks, TweakModifyType, FeatureFlagTweak, EligibilityTweak, AITweak, BasicPlistTweak
from tweaks.basic_plist_locations import FileLocation
from devicemanagement.constants import Device

from pymobiledevice3.exceptions import PyMobileDevice3Exception
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3 import usbmux
from pymobiledevice3.lockdown import create_using_usbmux

from pathlib import Path
import plistlib
import traceback

running = True
passed_check = False
num_tweaks = len(tweaks)

gestalt_path = Path.joinpath(Path.cwd(), "com.apple.MobileGestalt.plist")
flags_path = Path.joinpath(Path.cwd(), "Global.plist")
device = None

def print_option(num: int, active: bool, message: str):
    txt = str(num) + ". "
    if active:
        txt = txt + "[Y] "
    txt = txt + message
    print(txt)

def get_apply_number(num: int) -> int:
    return num + 5-num%5

while running:
    print("""\n\n\n\n
                                                                      
         ,--.                                                         
       ,--.'|                                                 ___     
   ,--,:  : |                                               ,--.'|_   
,`--.'`|  ' :         ,--,                                  |  | :,'  
|   :  :  | |       ,'_ /|  ,----._,.  ,----._,.            :  : ' :  
:   |   \\ | :  .--. |  | : /   /  ' / /   /  ' /   ,---.  .;__,'  /   
|   : '  '; |,'_ /| :  . ||   :     ||   :     |  /     \\ |  |   |    
'   ' ;.    ;|  ' | |  . .|   | .\\  .|   | .\\  . /    /  |:__,'| :    
|   | | \\   ||  | ' |  | |.   ; ';  |.   ; ';  |.    ' / |  '  : |__  
'   : |  ; .':  | : ;  ; |'   .   . |'   .   . |'   ;   /|  |  | '.'| 
|   | '`--'  '  :  `--'   \\`---`-'| | `---`-'| |'   |  / |  ;  :    ; 
'   : |      :  ,      .-./.'__/\\_: | .'__/\\_: ||   :    |  |  ,   /  
;   |.'       `--`----'    |   :    : |   :    : \\   \\  /    ---`-'   
'---'                       \\   \\  /   \\   \\  /   `----'              
                             `--`-'     `--`-'                        
    """)
    print("CLI v3.0")
    print("by LeminLimez")
    print("Thanks @disfordottie for the clock animation and @lrdsnow for EU Enabler\n")
    print("Please back up your device before using!")

    while device == None:
        connected_devices = usbmux.list_devices()
        # Connect via usbmuxd
        for current_device in connected_devices:
            if current_device.is_usb:
                try:
                    ld = create_using_usbmux(serial=current_device.serial)
                    vals = ld.all_values
                    device = Device(uuid=current_device.serial, name=vals['DeviceName'], version=vals['ProductVersion'], model=vals['ProductType'], locale=ld.locale, ld=ld)
                except Exception as e:
                    print(traceback.format_exc())
                    input("Press Enter to continue...")
        
        if device == None:
            print("Please connect your device and try again!")
            input("Press Enter to continue...")

    print(f"Connected to {device.name}\niOS {device.version}\n")
    
    if not passed_check and Path.exists(gestalt_path) and Path.is_file(gestalt_path):
        passed_check = True
    
    if passed_check:
        count = 0
        for key in tweaks:
            count += 1
            # do not show if the tweak is not compatible
            if tweaks[key].is_compatible(device.version):
                print_option(count, tweaks[key].enabled, tweaks[key].label)
                if tweaks[key].divider_below:
                    print()

        # apply will still be the number of tweaks just to keep consistency
        print(f"\n{get_apply_number(num_tweaks + 1)}. Apply")
        print(f"{get_apply_number(num_tweaks + 1) + 1}. Remove All Tweaks")
        print(f"{get_apply_number(num_tweaks + 1) + 2}. Reset Mobile Gestalt")
        print("0. Exit\n")
        page = int(input("Enter a number: "))
        if page == get_apply_number(num_tweaks + 1) or page == get_apply_number(num_tweaks + 1) + 1:
            # either apply or reset tweaks
            print()
            resetting = page == (get_apply_number(num_tweaks + 1) + 1)
            # set the tweaks and apply
            # first open the file in read mode
            with open(gestalt_path, 'rb') as in_fp:
                gestalt_plist = plistlib.load(in_fp)
            # create the other plists
            flag_plist: dict = {}
            eligibility_files = None
            ai_file = None
            basic_plists: dict = {}

            # verify the device credentials before continuing
            if gestalt_plist["CacheExtra"]["qNNddlUK+B/YlooNoymwgA"] != device.version or gestalt_plist["CacheExtra"]["0+nc/Udy4WNG8S+Q7a/s1A"] != device.model:
                print("com.apple.mobilegestalt.plist does not match the device!")
                print("Please make sure you are using the correct file!")
                print("If you believe this is a mistake, you can override this check.")
                override = input("Do you want to overrride? (y/n) ")
                if override.lower() != 'y':
                    continue # break applying and return to the main page
            
            # set the plist keys
            if not resetting:
                for tweak in tweaks.values:
                    if isinstance(tweak, FeatureFlagTweak):
                        flag_plist = tweak.apply_tweak(flag_plist)
                    elif isinstance(tweak, EligibilityTweak):
                        tweak.set_region_code(device.locale[-2:])
                        eligibility_files = tweak.apply_tweak()
                    elif isinstance(tweak, AITweak):
                        ai_file = tweak.apply_tweak()
                    elif isinstance(tweak, BasicPlistTweak):
                        basic_plists = tweak.apply_tweak(basic_plists)
                    else:
                        gestalt_plist = tweak.apply_tweak(gestalt_plist)

            # create the restore file list
            files_to_restore = [
                FileToRestore(
                    contents=plistlib.dumps(gestalt_plist),
                    restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/",
                    restore_name="com.apple.MobileGestalt.plist"
                ),
                FileToRestore(
                    contents=plistlib.dumps(flag_plist),
                    restore_path="/var/preferences/FeatureFlags/",
                    restore_name="Global.plist"
                )
            ]
            if eligibility_files != None:
                files_to_restore += eligibility_files
            if ai_file != None:
                files_to_restore.append(ai_file)
            for location, plist in basic_plists:
                files_to_restore.append(FileToRestore(
                    contents=plistlib.dumps(plist),
                    restore_path=location.value
                ))
            # reset basic tweaks
            if resetting:
                empty_data = plistlib.dumps({})
                for location in FileLocation:
                    files_to_restore.append(FileToRestore(
                        contents=empty_data,
                        restore_path=location.value
                    ))
            # restore to the device
            try:
                restore_files(files=files_to_restore, reboot=True, lockdown_client=device.ld)
            except Exception as e:
                print(traceback.format_exc())
            finally:
                input("Press Enter to exit...")
                running = False
        elif page == get_apply_number(num_tweaks + 1) + 2:
            # reset mobilegestalt
            # restore to the device
            try:
                restore_files(files=[FileToRestore(
                    contents=b"",
                    restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/",
                    restore_name="com.apple.MobileGestalt.plist"
                )], reboot=True, lockdown_client=device.ld)
            except Exception as e:
                print(traceback.format_exc())
            finally:
                input("Press Enter to exit...")
                running = False
        elif page == 0:
            # exit the panel
            print("Goodbye!")
            running = False
        else:
            tweak = list(tweaks.values())[page-1]
            if page > 0 and page <= num_tweaks and tweak.is_compatible(device.version):
                if tweak.edit_type == TweakModifyType.TEXT:
                    # text input
                    inp_txt = ""
                    print(f"\n\n{tweak.label}")
                    print("Leave blank to turn off.\n")
                    if tweak.label == "Set Device Model Name":
                        inp_txt = "Enter Model Name: "
                    elif tweak.label == "Set Lock Screen Footnote Text":
                        inp_txt = "Enter Footnote: "
                    new_txt = input(inp_txt)
                    if new_txt == "":
                        tweak.set_enabled(False)
                    else:
                        tweak.set_value(new_txt)
                elif tweak.edit_type == TweakModifyType.PICKER:
                    # pick between values
                    print("\n\nSelect a value.")
                    print("If you do not know which to try, start with the first option.")
                    values = tweak.value
                    for option in range(len(values)):
                        print_option(
                                num=option+1,
                                active=(tweak.enabled and tweak.get_selected_option() == option),
                                message=str(values[option])
                            )
                    print_option(num=len(values)+1, active=(not tweak.enabled), message="Disable")
                    picker_choice = int(input("Select option: "))
                    if picker_choice > 0 and picker_choice <= len(values):
                        tweak.set_selected_option(picker_choice-1)
                    elif picker_choice == len(values)+1:
                        tweak.set_enabled(False)
                else:
                    tweak.toggle_enabled()
    else:
        print("No MobileGestalt file found!")
        print(f"Please place the file in \'{Path.cwd()}\' with the name \'com.apple.MobileGestalt.plist\'")
        print("Remember to make a backup of the file!!\n")
        print("1. Retry")
        print("2. Enter path\n")
        choice = int(input("Enter number: "))
        if choice == 2:
            new_path = input("Enter new path to file: ")
            gestalt_path = Path(new_path)
