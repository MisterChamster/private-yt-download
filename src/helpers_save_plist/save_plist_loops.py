from src.helpers_save_plist.save_plist_askers_numbering import (ask_numbering_main_menu,
                                                                ask_first_number,
                                                                ask_last_number)
from src.helpers_save_plist.save_plist_askers_trim_elements import(ask_trimming_main_menu,
                                                                   ask_custom_trim,
                                                                   ask_el_trim,
                                                                   ask_multiple_trim,)
from src.helpers_save_plist.save_plist_utils import (list_vids,
                                                     del_by_number,
                                                     del_by_range,
                                                     list_vids_custom_url,
                                                     list_vid_names)
from src.helpers_save_plist.save_plist_askers_trim_names import (ask_trim_names_main_menu,
                                                                 ask_length_type,
                                                                 ask_length_int,
                                                                 ask_length_str,
                                                                 ask_el_name_trim,
                                                                 ask_multiple_name_trim)



def trim_vids_loop(plist_list: list) -> list:
    while True:
        action = ask_trimming_main_menu()
        print()

        if action == "all":
            return plist_list

        elif action == "custom":
            plist_list = custom_trim_loop(plist_list)
            if plist_list == None:
                return None

        elif action == "list":
            list_vids(plist_list)
            print()


def custom_trim_loop(plist_list: list) -> list:
    while True:
        if not plist_list:
            print("All elements have been removed.\n\n")
            return None

        list_vids(plist_list)
        print()

        action = ask_custom_trim()
        print()

        if action == "trim_element":
            plist_numbers = [i[0] for i in plist_list]
            number_to_trim = ask_el_trim(plist_numbers)
            print()
            if number_to_trim is None:
                continue
            plist_list = del_by_number(plist_list, number_to_trim)

        elif action == "trim_range":
            plist_numbers = [i[0] for i in plist_list]
            trim_range = ask_multiple_trim(plist_numbers)
            print()
            if trim_range is None:
                continue
            plist_list = del_by_range(plist_list, trim_range[0], trim_range[1])

        elif action == "return":
            return plist_list


def numbering_loop(plist_list: list) -> list:
    og_numbering = [el[0] for el in plist_list]
    final_numbering = og_numbering
    while True:
        print("Current numbering:")
        list_vids_custom_url(plist_list, final_numbering)
        print()

        action = ask_numbering_main_menu()
        print()

        if action == "start_on_1":
            final_numbering = [i+1 for i in range(0, len(og_numbering))]
            print()

        elif action == "no_numbering":
            final_numbering = None
            print()

        elif action == "begin_on_integer":
            first_el_num = ask_first_number()
            print()
            if first_el_num == None:
                continue
            final_numbering = [i for i in range(first_el_num, first_el_num+len(og_numbering))]

        elif action == "end_on_integer":
            last_el_num = ask_last_number(len(og_numbering))
            print()
            if last_el_num == None:
                continue
            final_numbering = [i for i in range(last_el_num-len(og_numbering)+1, last_el_num+2)]

        elif action == "reverse_numbering":
            final_numbering = final_numbering[::-1]
            print()

        elif action == "original_numbering":
            final_numbering = og_numbering
            print()

        elif action == "save":
            print()
            return final_numbering


# START WORK HERE
def trim_names_loop(plist_list: list) -> list:
    og_names = [el[1] for el in plist_list]
    final_names = og_names
    while True:
        print("Current names:")
        list_vid_names(final_names)
        print()

        action = ask_trim_names_main_menu()
        print()

        if action == "trim_all_start":
            trim_len = get_trim_length_loop()
            if trim_len == None:
                continue
            for el in final_names:
                el = el[trim_len:]

        elif action == "trim_all_end":
            trim_len = get_trim_length_loop()
            if trim_len == None:
                continue
            for el in final_names:
                el = el[:trim_len]

        elif action == "trim_range":
            trim_len = get_trim_length_loop()
            if trim_len == None:
                continue
            pass

        elif action == "trim_specific":
            trim_len = get_trim_length_loop()
            if trim_len == None:
                continue
            pass

        elif action == "original_names":
            final_names = og_names

        elif action == "save":
            return final_names


def get_trim_length_loop() -> int:
    trim_len = 0
    while True:
        input_type = ask_length_type()

        if input_type == "input_integer":
            trim_len = ask_length_int()
            if trim_len == None:
                return None
            return trim_len

        elif input_type == "input_string":
            trim_len = ask_length_str()
            if trim_len == None:
                return None
            return trim_len

        elif input_type == "return":
            return None
