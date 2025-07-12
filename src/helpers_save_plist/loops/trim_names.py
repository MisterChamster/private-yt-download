from src.helpers_save_plist.utils import list_vid_names
from src.helpers_save_plist.askers.trim_names import (ask_trim_names_main_menu,
                                                      ask_length_type,
                                                      ask_length_int,
                                                      ask_length_str,
                                                      ask_el_name_trim,
                                                      ask_multiple_name_trim)



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
            print()
            if trim_len == None:
                continue
            for el in final_names:
                el = el[:trim_len]

        elif action == "trim_range":
            trim_len = get_trim_length_loop()
            print()
            if trim_len == None:
                continue
            # START WORK HERE
            pass

        elif action == "trim_specific":
            trim_len = get_trim_length_loop()
            print()
            if trim_len == None:
                continue
            # START WORK HERE
            pass

        elif action == "original_names":
            final_names = og_names

        elif action == "save":
            return final_names


def get_trim_length_loop() -> int:
    trim_len = 0
    while True:
        input_type = ask_length_type()
        print()

        if input_type == "input_integer":
            trim_len = ask_length_int()
            print()
            if trim_len == None:
                return None
            return trim_len

        elif input_type == "input_string":
            trim_len = ask_length_str()
            print()
            if trim_len == None:
                return None
            return trim_len

        elif input_type == "return":
            return None
