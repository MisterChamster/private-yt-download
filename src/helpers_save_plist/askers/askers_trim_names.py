def ask_trim_names_main_menu() -> str:
    returns_dict = {"tas": "trim_all_start",
                    "tae": "trim_all_end",
                    "tr":  "trim_range",
                    "ts":  "trim_specific",
                    "og":  "original_names",
                    "s":   "save"}
    while True:
        print("Choose element name trimming option:\n" \
              "tas - Trim all names at the start...\n" \
              "tae - Trim all names at the end...\n" \
              "tr  - Trim name of elements in range... \n" \
              "ts  - Trim name of a specific element...\n" \
              "og  - Return all elements to original names\n" \
              "s   - Save\n>> ", end="")
        asker = str(input())

        if asker not in ["tas", "tae", "tr", "ts", "og", "s"]:
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
        else:
            return int(asker)


def ask_length_str() -> str:
    while True:
        print("Input string to cut (will count its characters):\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        return asker


def ask_el_name_trim() -> int:
    return


def ask_multiple_name_trim() -> list:
    return
