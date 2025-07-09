from src.helpers_save_plist.askers_plist import (ask_trimming_main_menu,
                                                 ask_custom_trim,
                                                 ask_el_trim)
from src.helpers_save_plist.save_plist_utils import (list_vids,
                                                     del_by_number)



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
            # START WORK HERE
            # List all elements first
            number_to_trim = ask_el_trim()
            print()
            if number_to_trim is None:
                continue
            number_to_trim = int(number_to_trim)
            if number_to_trim == 0 or number_to_trim > len(plist_list):
                print("Number is not an element on videos list.")
            else:
                plist_list = del_by_number(plist_list, number_to_trim)
        elif action == "tr":
            # List all elements first
            pass
        elif action == "ls":
            list_vids(plist_list)
            print()
        elif action == "rt":
            return plist_list
