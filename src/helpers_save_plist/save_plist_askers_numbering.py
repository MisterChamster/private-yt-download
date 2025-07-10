def ask_numbering(min_el_index, max_el_index):
    """
    Determines numbering in filenames.

    In series of questions, function determines if elements should be numbered, 
    and if so, in what order and on what number will the numbering start.

    Args:
        min_el_index (int): Index of the first element to be numbered.
        max_el_index (int): Index of the last element to be numbered.

    Returns:
        list[a, b]: 
            a (str): Naming order ("asc", "desc", "not").
            b (int): Number of first downloaded element.
    """

    while True:
        print("Choose numbering option:\n" \
              "Enter   - Starting on 1\n" \
              "Integer - Starting on integer\n" \
              "n       - No numbering\n" \
              "c       - Custom numbering...\n>> ", end="")
        user_input = str(input())

        if user_input == "" or user_input == "y":
            return ["asc", 1]
        if user_input.isdigit():
            return ["asc", int(user_input)]
        if user_input == "n":
            return ["not", -1]
        if user_input == "c":
            if min_el_index != 0:
                user_input_custom = input("Choose custom numbering option (starting from element's number in playlist [n - normal order, r - reverse order], d - descending from...):\n>>").lower()
                if user_input_custom == "n":
                    return ["asc", min_el_index+1]
            else:
                user_input_custom = input("Choose custom numbering option (r - reverse order, d - descending from...):\n>>").lower()

            if user_input_custom == "r":
                return ["desc", max_el_index+1]
            if user_input_custom == "d":
                number_of_elements = max_el_index - min_el_index + 1
                desc_from = input(f"Files will be numbered in reversed order, starting from (not lower than {number_of_elements}):\n>>")
                if desc_from.isdigit():
                    desc_from = int(desc_from)
                    if desc_from >= number_of_elements:
                        return ["desc", desc_from]


def ask_numbering_main_menu():
    while True:
        print("Choose numbering option:\n" \
              "o  - Starting on 1\n" \
              "n  - No numbering\n" \
              "b  - Beginning on integer...\n" \
              "e  - Ending on integer...\n" \
              "r  - Reverse current numbering\n" \
              "og - Original numbering\n" \
              "s  - Save\n>> ", end="")
        action = str(input())

        if action not in ["o", "n", "b", "e", "r", "og", "s"]:
            print("Incorrect input.\n")
        return action


def ask_first_number():
    while True:
        print("Input the number of the first element:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
            continue

        first_el_num = int(asker)
        return first_el_num


def ask_last_number(plist_len):
    lowest_possible = plist_len - 1
    while True:
        print(f"Input the number of the last element ({lowest_possible} or higher):\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
            continue

        last_el_num = int(asker)
        if last_el_num < lowest_possible:
            print("Given number is too small.\n")
            continue
        return last_el_num
