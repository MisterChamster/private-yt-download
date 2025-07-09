from src.helpers_save_plist.askers_plist import (ask_trimming_main_menu,
                                                 ask_custom_trim,
                                                 ask_el_trim)
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

        if action == "te":
            number_to_trim = ask_el_trim()
            if number_to_trim == 0 or number_to_trim > len(plist_list):
                print("Number is not an element on videos list.")
            else:
                # WORK HERE
                # Create del_by_number(plist_list, number) that deletes an
                # element by number
                pass
        elif action == "tr":
            pass
        elif action == "ls":
            list_vids(plist_list)
            print()
        elif action == "rt":
            return plist_list
