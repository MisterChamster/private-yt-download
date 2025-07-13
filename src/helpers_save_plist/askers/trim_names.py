def ask_trim_names_main_menu() -> str:
    returns_dict = {"tan": "trim_all_elements",
                    "ts":  "trim_specific",
                    "tr":  "trim_range",
                    "og":  "original_names",
                    "s":   "save"}
    while True:
        print("Choose element name trimming option:\n" \
              "tan - Trim all names...\n" \
              "ts  - Trim name of a specific element...\n" \
              "tr  - Trim name of elements in range... \n" \
              "og  - Return all elements to original names\n" \
              "s   - Save\n>> ", end="")
        asker = str(input())

        if asker not in ["tan", "ts", "tr", "og", "s"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_length_type() -> str:
    returns_dict = {"i":  "input_integer",
                    "s":  "input_string",
                    "rt": "return"}
    while True:
        print("Choose trim length value type:\n" \
              "i  - Input integer value...\n" \
              "s  - Input string and calculate it's length...\n" \
              "rt - Return\n>> ", end="")
        asker = str(input())

        if asker not in ["i", "s", "rt"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_length_int() -> int:
    while True:
        print("Input a number of characters to cut:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
        asker_int = int(asker)
        if asker_int == 0:
            return None
        else:
            return int(asker)


def ask_length_str() -> str:
    while True:
        print("Input string to cut (will count its characters):\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit" or asker == "":
            return None
        return len(asker)


def ask_trim_front_back() -> str:
    returns_dict = {"s": "start",
                    "e": "end"}
    while True:
        print("Cut characters from (to exit input 'exit'):\n" \
              "s - start\n" \
              "e - end\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif asker not in ["s", "e"]:
            print("Incorrect input.\n")
        else:
            return returns_dict[asker]


def ask_el_name_trim(plist_numbers: list) -> int:
    while True:
        print("Input number of the element to trim name:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
            continue
        el_number = int(asker)
        if el_number not in plist_numbers:
            print("Number is not an element on videos list.\n")
        else:
            return el_number


def ask_multiple_name_trim(plist_numbers: list) -> list:
    return
