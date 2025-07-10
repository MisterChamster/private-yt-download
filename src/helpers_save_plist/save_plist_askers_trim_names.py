def ask_trim_names_main_menu():
    while True:
        print("Choose element name trimming option:\n" \
              "tas - Trim all names at the start...\n" \
              "tae - Trim all names at the end...\n" \
              "tre - Trim a range of elements... \n" \
              "tsv - Trim specific tracks by value...\n" \
              "og  - Return all elements to original names\n" \
              "s   - Save\n>> ", end="")
        asker = str(input())

        if asker not in ["tas", "tae", "tre", "tsv", "og", "s"]:
            print("Incorrect input.\n")
        else:
            return asker


def ask_length_type():
    while True:
        print("Choose trim length value type:\n" \
              "i  - Input integer value...\n" \
              "s  - Input string and calculate it's length...\n" \
              "rt - Return\n>> ", end="")
        asker = str(input())

        if asker not in ["i", "s", "rt"]:
            print("Incorrect input.\n")
        elif asker == "rt":
            return None
        else:
            return asker


def ask_length_int():
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


def ask_length_str():
    while True:
        print("Input string to cut (will count its characters):\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        return asker
