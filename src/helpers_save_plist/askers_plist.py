def ask_del_duplicates():
    user_input = " "
    while True:
        print("Duplicates detected. Choose handling option:\n" \
              "d - Delete duplicates\n" \
              "l - Leave duplicates\n>> ", end="")
        user_input = str(input())

        if user_input == "d":
            return True
        elif user_input == "l":
            return False


def ask_num_of_tracks(plist_len): 
    """
    Asks user which elements to download.

    If user presses enter, list from 0 to plist_len will be returned.
    If user inputs an integer, list from 0 to that integer will be returned.
    If user inputs c, they'll be asked to input number of first and last element. 
    [start-1, end] will be returned.
    Else, list from 0 to plist_len will be returned.
    When input is too big, small or incorrect, a default value will be assigned.

    Args:
        plist_len (int): Length of playlist considered.

    Returns:
        list[int, int]: Indexes of first and last element to be downloaded.
    """
    print("Choose elements to download:\n" \
          "Enter   - All elements\n" \
          "Integer - Number of elements from start\n" \
          "c       - Custom settings...\n>> ", end="")
    num = str(input())
    if num == '':
        return [0, plist_len]

    elif num == 'c':
        start = input("Starting from element:\n>>")
        if not start.isdigit():
            print("Starting from the beginning.")
            start = 0
        elif int(start) > plist_len or int(start) < 1:
            print("Starting from the beginning.")
            start = 0
        else:
            start = int(start) - 1

        end = input("Ending on element:\n>>")  
        if not end.isdigit():
            print("Ending at the end.")
            end = plist_len
        elif int(end) < start or int(end) > plist_len:
            print("Ending at the end.")
            end = plist_len
        else:
            end = int(end)
        return [start, end]

    elif num.isdigit() and int(num) <= plist_len:
        return [0, int(num)]

    elif num.isdigit() and int(num) > plist_len:
        print("Number inputted by You is too big! Downloading all the tracks.\n")
        return [0, plist_len]

    else:
        print("Downloading whole playlist.\n")
        return [0, plist_len]


def ask_trimming_main_menu():
    while True:
        print("Choose which elements to download:\n" \
              "Enter - All current elements\n" \
              "c     - Custom settings...\n" \
              "ls    - List all current elements\n>> ", end="")
        asker = str(input())

        if not asker in ["", "c", "ls"]:
            print("Incorrect input.\n")
        else:
            if asker == "":
                return "all"
            return asker


def ask_custom_trim():
    while True:
        print("Choose custom trimming option:\n" \
              "te    - Trim one element\n" \
              "tr    - Trim a range of elements\n" \
              "rt    - Return\n>> ", end="")
        asker = str(input())

        if asker not in ["te", "tr", "rt"]:
            print("Incorrect input.\n")
        else:
            return asker


def ask_el_trim(plist_len):
    while True:
        print("Input number of the element to trim:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
        asker = int(asker)
        if asker == 0 or asker > plist_len:
            print("Number is not an element on videos list.\n")
        else:
            return asker


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
    user_input = " "

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


def ask_read_trim_lens():
    """
    Asks user about cutting names of the elements.

    Returns:
        list[a, b]:
            a (int): Number of letters cut from the start of filename.
            b (int): Number of letters cut from the end of filename.
    """
    inputSC = " "
    namecut_list = [0, 0]
    while inputSC not in ["", "s", "b", "e"]:
        print("Choose name trimming option:\n" \
              "Enter - No trimming\n" \
              "s     - Trim at the start\n" \
              "e     - Trim at the end\n" \
              "b     - Trim on both sides\n>> ", end="")
        inputSC = str(input())

    if inputSC == "s":
        namecut_list[0] = str(input("Input the string or length You want to trim at the start:\n>>"))
        if namecut_list[0].isdigit():
            namecut_list[0] = int(namecut_list[0])
        else:
            namecut_list[0] = len(namecut_list[0])

    elif inputSC == "e":
        namecut_list[1] = str(input("Input the string or length You want to trim at the ending:\n>>"))
        if namecut_list[1].isdigit():
            namecut_list[1] = int(namecut_list[1])
        else:
            namecut_list[1] = len(namecut_list[1])

    elif inputSC == "b":
        namecut_list[0] = str(input("Input the string or length You want to trim at the start:\n>>"))
        if namecut_list[0].isdigit():
            namecut_list[0] = int(namecut_list[0])
        else:
            namecut_list[0] = len(namecut_list[0])

        namecut_list[1] = str(input("Input the string or length You want to trim at the ending:\n>>"))
        if namecut_list[1].isdigit():
            namecut_list[1] = int(namecut_list[1])
        else:
            namecut_list[1] = len(namecut_list[1])

    return namecut_list
