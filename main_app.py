from exploit.restore import restore_file
from pathlib import Path
import plistlib
import traceback
from pymobiledevice3.lockdown import create_using_usbmux
from packaging.version import parse


lockdown = create_using_usbmux()
model = lockdown.product_type
version = parse(lockdown.product_version)

if version < parse("17.0"):
    compatible = False
else:
    compatible = True

if model == ("iPhone10,1" or "iPhone10,2" or "iPhone10,3" or "iPhone10,4" or "iPhone12,8" or "iPhone14,6"):
    homeButton = True
else:
    homeButton = False

running = True
passed_check = False
# tweaks
dynamic_island_enabled = False
current_model_name = ""
boot_chime_enabled = False
charge_limit_enabled = False
stage_manager_enabled = False
xgestures_enabled = False

gestalt_path = Path.joinpath(Path.cwd(), "com.apple.MobileGestalt.plist")

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
    print("by LeminLimez")
    print("v1.0\n\n")
    
    if not passed_check and Path.exists(gestalt_path) and Path.is_file(gestalt_path):
        passed_check = True
    
    if not compatible:
        input(f"WARNING\n Nugget is intended for iOS 17.0 and newer.\nYou can cause SERIOUS damage to your device by using this on {version},\n You have been warned. We are not responsible for ANY damage caused to your device.")

    if passed_check:
        print(f"1. {"[Y] " if dynamic_island_enabled else ""}Toggle Dynamic Island")
        print(f"2. {"[Y] " if current_model_name != "" else ""}Set Device Model Name")
        print(f"3. {"[Y] " if boot_chime_enabled else ""}Toggle Boot Chime")
        print(f"4. {"[Y] " if charge_limit_enabled else ""}Toggle Charge Limit")
        print(f"5. {"[Y] " if stage_manager_enabled else ""}Toggle Stage Manager Supported")
        if homeButton:
            print(f"6. {"[Y] " if xgestures_enabled else ""}Toggle iPhone X gestures")
        print("\n9. Apply")
        print("0. Exit\n")
        page = int(input("Enter a number: "))
        if page == 1:
            dynamic_island_enabled = not dynamic_island_enabled
        elif page == 2:
            print("\n\nSet Model Name")
            print("Leave blank to turn off custom name.\n")
            name = input("Enter Model Name: ")
            current_model_name = name
        elif page == 3:
            boot_chime_enabled = not boot_chime_enabled
        elif page == 4:
            charge_limit_enabled = not charge_limit_enabled
        elif page == 5:
            stage_manager_enabled = not stage_manager_enabled
        elif page == 6:
            if homeButton:
                xgestures_enabled = not xgestures_enabled
        elif page == 9:
            print()
            # set the tweaks and apply
            # first open the file in read mode
            with open(gestalt_path, 'rb') as in_fp:
                plist = plistlib.load(in_fp)
            
            # set the plist keys
            if dynamic_island_enabled:
                plist["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["ArtworkDeviceSubType"] = 2556
            if current_model_name != "":
                plist["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["ArtworkDeviceProductDescription"] = current_model_name
            if boot_chime_enabled:
                plist["CacheExtra"]["QHxt+hGLaBPbQJbXiUJX3w"] = True
            if charge_limit_enabled:
                plist["CacheExtra"]["37NVydb//GP/GrhuTN+exg"] = True
            if stage_manager_enabled:
                plist["CacheExtra"]["qeaj75wk3HF4DwQ8qbIi7g"] = 1
            if xgestures_enabled:
                plist["CacheExtra"]["oPeik/9e8lQWMszEjbPzng"]["ArtworkDeviceSubType"] = 2436

            # write back to the file
            with open(gestalt_path, 'wb') as out_fp:
                plistlib.dump(plist, out_fp)
            # restore to the device
            try:
                restore_file(fp=gestalt_path, restore_path="/var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/", restore_name="com.apple.MobileGestalt.plist")
                input("Success! Reboot your device to see the changes.")
            except Exception as e:
                print(traceback.format_exc())
                input("Press Enter to continue...")
            running = False
        elif page == 0:
            # exit the panel
            print("Goodbye!")
            running = False
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