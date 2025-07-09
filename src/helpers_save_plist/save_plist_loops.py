from src.helpers_save_plist.askers_plist import ask_trimming_main_menu
from src.helpers_save_plist.save_plist_utils import list_vids

def trim_plist_loop(plist_list):
    while True:
        menu_option = ask_trimming_main_menu()
        print()
        if menu_option == "all":
            return plist_list
        elif menu_option == "c":
            #work here
            return
        if menu_option == "ls":
            list_vids(plist_list)
            print()
        elif menu_option == "rt":
            return plist_list
