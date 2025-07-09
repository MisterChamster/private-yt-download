from src.helpers_save_plist.askers_plist import (ask_trimming_main_menu,
                                                 ask_custom_trim)
from src.helpers_save_plist.save_plist_utils import list_vids

def trim_plist_loop(plist_list):
    while True:
        action = ask_trimming_main_menu()
        print()
        if action == "all":
            return plist_list
        elif action == "c":
            plist_list = custom_trim_loop(plist_list)
        elif action == "ls":
            list_vids(plist_list)
            print()


def custom_trim_loop(plist_list):
    while True:
        action = ask_custom_trim()
        print()

        # WORK HERE
        if action == "te":
            pass
        elif action == "tr":
            pass
        elif action == "ls":
            list_vids(plist_list)
            print()
        elif action == "rt":
            return plist_list
