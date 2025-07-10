from src.helpers_save_plist.askers_plist import (ask_trimming_main_menu,
                                                 ask_custom_trim,
                                                 ask_el_trim,
                                                 ask_multiple_trim,
                                                 ask_numbering_main_menu,
                                                 ask_first_number)
from src.helpers_save_plist.save_plist_utils import (list_vids,
                                                     del_by_number,
                                                     del_by_range,
                                                     list_vids_custom_url)



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
        print("Current numbering:")
        list_vids_custom_url(plist_list, final_numbering)
        print()

        action = ask_numbering_main_menu()
        if action == "o":
            final_numbering = [i+1 for i in range(0, len(og_numbering))]
            print()
        elif action == "n":
            final_numbering = []
            print()
        elif action == "b":
            first_el_num = ask_first_number()
            if first_el_num == None:
                print()
                continue
            final_numbering = [i for i in range(first_el_num, first_el_num+len(og_numbering))]
            # Test it
        elif action == "e":
            # Ask for last element (asker)
            pass
        elif action == "r":
            final_numbering = final_numbering[::-1]
            print()
        elif action == "og":
            final_numbering = og_numbering
            print()
        elif action == "s":
            print()
            return plist_list
