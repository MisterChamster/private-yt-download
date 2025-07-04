def ask_url_and_type():
    """
    Asks user for URL, checks if it's valid and determines action.

    Returns:
        list[a, b]:
            a (str): URL inputted by user
            b (str): Action type
    """
    url = str(input("Enter URL: \n>> "))
    if (len(url) > 34 and url[:34] == 'https://youtube.com/playlist?list='):
        inputDE = " "
        while inputDE not in ["", "d", "e"]:
            inputDE = input("What do You want to do with playlist? (Enter - download, e - extract playlist data)\n>>").lower()
        if inputDE == "e":
            return [url, "extract"]
        return [url, 'plist']

    elif (len(url) > 17 and url[:17] == 'https://youtu.be/') or \
         (len(url) > 29 and url[:29] == 'https://www.youtube.com/watch'):
        if '&list=' in url:
            url = url[:url.find('&list=')]
        return [url, 'single']

    else:
        print("Invalid URL!\n")
        return [url, 'invalid']


def ask_save_ext():
    """
    Asks user for extension.

    In infinite loop, forces user to input either 4, 3 or f 
    to get proper extension.

    Returns:
        str: Extenstion chosen by user.
    """
    user_input = " "
    format_dict = {"4": "mp4", "3": "mp3", "f": "flac"}
    while user_input not in format_dict:
        user_input = input("What format do You want to save as? (4 - mp4, 3 - mp3, f - flac)\n>>").lower()

    return format_dict[user_input]


def ask_del_duplicates():
    """
    Asks user what to do in case duplicates appear in playlist.

    Returns:
        boolean: True - delete duplicates, False - leave duplicates.
    """

    user_input = " "
    dupl_dict = {"": True, "d": True, "l": False}
    while user_input not in dupl_dict:
        user_input = input("Duplicates detected. What should be done about them? (Enter - delete, l - leave)\n>>").lower()

    return dupl_dict[user_input]


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
    num = input("How to download the elements? (Enter - all, integer number - number of elements from start, c - custom settings...)\n>>").lower()
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
        user_input = input("Do You want elements to be numbered? (Enter - starting on 1, integer - starting on integer, n - no, c - custom...)\n>>").lower()

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


def ask_extract_write_order():
    """
    Asks user for extract order.

    Returns:
        string: "asc" or "desc".
    """
    order = ""
    result_dict = {"a": "asc", "d": "desc"}
    while order not in result_dict:
        order = input("In what order do You want to write elements to file? (a - ascending, d - descending)\n>>").lower()
    return result_dict[order]


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
        inputSC = input("Do You want to trim names of all elements? (Enter - no, s - at the start, e - at the end, b - both)\n>>").lower()

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
