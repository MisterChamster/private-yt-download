from src.helpers_save_plist.askers_plist import (ask_trimming_main_menu,
                                                 ask_custom_trim,
                                                 ask_el_trim,
                                                 ask_multiple_trim,
                                                 ask_numbering_main_menu)
from src.helpers_save_plist.save_plist_utils import (list_vids,
                                                     del_by_number,
                                                     del_by_range)



def trim_plist_loop(plist_list):
    while True:
        action = ask_trimming_main_menu()
        print()

        if action == "all":
            return plist_list

        elif action == "c":
            plist_list = custom_trim_loop(plist_list)
            if plist_list == None:
                return None

        elif action == "ls":
            list_vids(plist_list)
            print()


def custom_trim_loop(plist_list):
    while True:
        if not plist_list:
            print("All elements have been removed.\n\n")
            return None

        list_vids(plist_list)
        print()

        action = ask_custom_trim()
        print()

        if action == "te":
            plist_numbers = [i[0] for i in plist_list]
            number_to_trim = ask_el_trim(plist_numbers)
            if number_to_trim is None:
                continue
            print()
            plist_list = del_by_number(plist_list, number_to_trim)

        elif action == "tr":
            plist_numbers = [i[0] for i in plist_list]
            trim_range = ask_multiple_trim(plist_numbers)
            if trim_range is None:
                continue
            print()
            plist_list = del_by_range(plist_list, trim_range[0], trim_range[1])

        elif action == "rt":
            return plist_list


def numbering_loop(plist_list):
    og_numbering = [el[0] for el in plist_list]
    final_numbering = og_numbering
    while True:
        action = ask_numbering_main_menu()
        return plist_list
