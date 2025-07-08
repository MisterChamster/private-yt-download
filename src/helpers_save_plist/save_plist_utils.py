from src.common.utils import illegal_char_remover



def zeros_at_beginning(number, max_element_number):
    """
    Determines a number in name of element present in a playlist.

    Depending on number of max element, function will put an adequate number of 0's
    before the index.

    Examples:
        (plist_len = 4):        01, 02, 03, 04
        (plist_len = 64):    ...08, 09, 10, 11,...
        (plist_len = 128):   ...008, 009, 010, 011,..., 098, 099, 100, 101,...

    Args:
        number (int):               number of element in playlist.
        max_element_number (int):   max number that'll be used.

    Returns:
        str: zeros determined by function + number + ". "
    """
    return ((max_element_number < 10) * f"0{number}. ") + ((max_element_number >= 10) * (f"{(len(str(max_element_number)) - len(str(number))) * '0'}{number}. ")) # I'm really sorry. The same code is written below, but it's readable
    if max_element_number < 10:
        return f"0{number}. "
    else:
        digits_of_biggest_number    = len(str(max_element_number))
        digits_of_number            = len(str(number))
        gg                          = digits_of_biggest_number - digits_of_number
        return f"{gg * '0'}{number}. "


def del_duplicates_from_listoflists(list_of_lists):
    """
    Deletes duplicate lists from a list of lists.

    Args:
        list_of_lists (list): Self explainatory.

    Returns:
        list: list_of_lists without duplicates.
    """
    i = 0
    while i + 1 < len(list_of_lists):
        a = i + 1
        while a < len(list_of_lists):
            if list_of_lists[i][0] == list_of_lists[a][0] and list_of_lists[i][1] == list_of_lists[a][1]:
                list_of_lists.pop(a)
            else:
                a += 1
        i += 1

    return list_of_lists


def get_indexes_of_searched_item(list_of_items, searched_item):
    indexes_list = []
    i = 0
    while i < len(list_of_items):
        if list_of_items[i] == searched_item:
            indexes_list.append(i)
        i += 1
    return indexes_list


def are_duplicates(list_of_items):
    i = 0
    while i+1 < len(list_of_items):
        item_appearances = get_indexes_of_searched_item(list_of_items, list_of_items[i])
        if len(item_appearances) > 1:
            print("Duplicates:")
            print(item_appearances)
            return True
        i += 1
    return False


def get_indexes_of_duplicates(list_of_items):
    list_of_appearances = []
    list_of_lists_of_appearances = []
    i = 0
    while i+1 < len(list_of_items):
        item_appearances = get_indexes_of_searched_item(list_of_items, list_of_items[i])
        if len(item_appearances) > 1:
            list_of_lists_of_appearances.append(item_appearances[1:])
        i += 1
    
    for item1 in list_of_lists_of_appearances:
        for item2 in item1:
            list_of_appearances.append(item2)
            list_of_appearances = list(set(list_of_appearances))
    return list_of_appearances


def name_file_on_plist(OGtitle, title_number, namecut_list):
    """
    Changes a string to match it with user's desired outcome.

    Trims the title if needed, removes illegal signs and adds index.
    Due to program's characteristics, function does not handle negative ints in namecut list.

    Args:
        title (str):                            Title of youtube video.
        titleindex (str):                       Numbering in filename (after adding zeros).
        namecut_list (list[a (int), b (int)]):  Number of characters to be cut from start end end of the title.

    Returns:
        str: Final name of a file.
    """
    lens = namecut_list[0]
    lene = namecut_list[1]
    policed_OGtitle = illegal_char_remover(OGtitle)

    #nothing remains after trimming name
    if (lens + lene >= len(OGtitle) or lens >= len(OGtitle) or lene > len(OGtitle)) and title_number == "":
        if len(policed_OGtitle) != len(OGtitle):
            print(f"Length of a trim is larger than the title. Returning original title with illegal chars removed...")
        else:
            print("Length of a trim is larger than the title. Returning original title...")
        return policed_OGtitle
    
    if lene == 0:
        ret_title = OGtitle[lens:]
    else:
        ret_title = OGtitle[lens:-lene]
    policed_ret_title = illegal_char_remover(ret_title)

    if len(policed_OGtitle) != len(OGtitle):
        print(f"{OGtitle} - has been updated to not contain illegal characters")
    return title_number + policed_ret_title
