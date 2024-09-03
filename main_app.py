from exploit.restore import restore_file
from pathlib import Path
import plistlib
import traceback

running = True
passed_check = False
# tweaks
dynamic_island_enabled = False
current_model_name = ""
boot_chime_enabled = False
charge_limit_enabled = False
stage_manager_enabled = False
shutter_sound_enabled = False
always_on_display_enabled = False
apple_pencil_enabled = False
action_button_enabled = False
internal_storage_enabled = False

gestalt_path = Path.joinpath(Path.cwd(), "com.apple.MobileGestalt.plist")

def print_option(num: int, active: bool, message: str):
    txt = str(num) + ". "
    if active:
        txt = txt + "[Y] "
    txt = txt + message
    print(txt)

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
    print("v1.2\n\n")
    print("\nPlease back up your device before using!")
    
    if not passed_check and Path.exists(gestalt_path) and Path.is_file(gestalt_path):
        passed_check = True
    
    if passed_check:
        print_option(1, dynamic_island_enabled, "Toggle Dynamic Island")
        print_option(2, current_model_name != "", "Set Device Model Name")
        print_option(3, boot_chime_enabled, "Toggle Boot Chime")
        print_option(4, charge_limit_enabled, "Toggle Charge Limit")
        print_option(5, stage_manager_enabled, "Toggle Stage Manager Supported")
        print_option(6, shutter_sound_enabled, "Disable Region Restrictions (ie. Shutter Sound)")
        print_option(7, always_on_display_enabled, "Always On Display (iOS 18+ only)")
        print_option(8, apple_pencil_enabled, "Toggle Apple Pencil")
        print_option(9, action_button_enabled, "Toggle Action Button")
        print_option(10, internal_storage_enabled, "Toggle Internal Storage")
        print("\n11. Apply")
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
            shutter_sound_enabled = not shutter_sound_enabled
        elif page == 7:
            always_on_display_enabled = not always_on_display_enabled
        elif page == 8:
            apple_pencil_enabled = not apple_pencil_enabled
        elif page == 9:
            action_button_enabled = not action_button_enabled
        elif page == 10:
            internal_storage_enabled = not internal_storage_enabled
        elif page == 11:
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
            if shutter_sound_enabled:
                plist["CacheExtra"]["h63QSdBCiT/z0WU6rdQv6Q"] = "US"
                plist["CacheExtra"]["zHeENZu+wbg7PUprwNwBWg"] = "LL/A"
            if always_on_display_enabled:
                plist["CacheExtra"]["2OOJf1VhaM7NxfRok3HbWQ"] = True
                plist["CacheExtra"]["j8/Omm6s1lsmTDFsXjsBfA"] = True
            if apple_pencil_enabled:
                plist["CacheExtra"]["yhHcB0iH0d1XzPO/CFd3ow"] = True
            if action_button_enabled:
                plist["CacheExtra"]["cT44WE1EohiwRzhsZ8xEsw"] = True
            if internal_storage_enabled:
                plist["CacheExtra"]["LBJfwOEzExRxzlAnSuI7eg"] = True

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
