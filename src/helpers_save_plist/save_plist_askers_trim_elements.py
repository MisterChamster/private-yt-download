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
              "te    - Trim one element...\n" \
              "tr    - Trim a range of elements...\n" \
              "rt    - Return\n>> ", end="")
        asker = str(input())

        if asker not in ["te", "tr", "rt"]:
            print("Incorrect input.\n")
        else:
            return asker


def ask_el_trim(plist_numbers):
    while True:
        print("Input number of the element to trim:\n" \
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


def ask_multiple_trim(plist_numbers):
    while True:
        print("Input number of the first element to trim:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker = str(input())

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
            continue

        start_el = int(asker)
        if start_el not in plist_numbers:
            print("Number is not an element on videos list.\n")
        else:
            break

    print()

    while True:
        print("Input number of the last element to trim:\n" \
              "(to exit input 'exit')\n>> ", end="")
        asker2 = str(input())

        if asker2 == "exit":
            return None
        elif not asker2.isdigit():
            print("Incorrect input.\n")
            continue

        end_el = int(asker2)
        if end_el not in plist_numbers:
            print("Number is not an element on videos list.\n")
        elif end_el < start_el:
            print("End number can't be smaller than the start number.\n")
        else:
            return [start_el, end_el]
