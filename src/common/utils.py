from socket import create_connection



def determine_url_type(url):
    if (len(url) > 34 and url[:34] == 'https://youtube.com/playlist?list='):
        return 'plist'

    elif (len(url) > 17 and url[:17] == 'https://youtu.be/') or \
         (len(url) > 29 and url[:29] == 'https://www.youtube.com/watch'):
        return 'single'

    else:
        print("Invalid URL!\n")
        return 'invalid'


def is_internet_available():
    """
    Checks internet availability.

    Returns:
        True:   Internet is available.
        False:  Internet is not available
    """
    try:
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def illegal_char_remover(suspect_string):
    """
    Removes chars that are illegal in naming a file from string.

    From given string, function removes \\, /, :, *, ?, ", <, >, | 
    (chars illegal in naming files) and returns it.

    Args:
        suspect_string (str): String with potenetial characters to remove.

    Returns:
        str: Argument string without signs illegal in filenaming.
    """
    charlist = [a for a in suspect_string]
    i = 0
    while i < len(charlist):
        if charlist[i] in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
            charlist.pop(i)
        else:
            i += 1

    policedstring = "".join(charlist)
    if policedstring == "":
        return "Invalid title"
    return policedstring


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
    curr_el = 0
    while curr_el + 1 < len(list_of_lists):
        a = curr_el + 1
        while a < len(list_of_lists):
            if list_of_lists[curr_el][0] == list_of_lists[a][0] and list_of_lists[curr_el][1] == list_of_lists[a][1]:
                list_of_lists.pop(a)
            else:
                a += 1
        curr_el += 1
    
    return list_of_lists


def name_your_file(OGtitle, title_number, namecut_list):
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
    policed_OGtitle = char_police(OGtitle)

    #nothing remains after policing
    if policed_OGtitle == "" and title_number == "":
        return illegal_to_ascii(OGtitle)

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
    policed_ret_title = char_police(ret_title)

    if policed_ret_title == "" and title_number == "": #nothing remains after trimming and policing
        print("After trimming, title contains only illegal signs")
        return illegal_to_ascii(ret_title)

    if len(policed_OGtitle) != len(OGtitle):
        print(f"{OGtitle} - has been updated to not contain illegal characters")
    return title_number + policed_ret_title


def get_ydl_options(extension):
    ydl_opts = {"quiet": True}
    if extension == "mp4":
        ydl_opts["merge_output_format"] = "mp4"
        ydl_opts["format"] = "bestvideo+bestaudio/best"
    elif extension == "mp3":
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio",
                                       "preferredcodec": "mp3"}]
        ydl_opts["format"] = "bestaudio"
    elif extension == "flac":
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio",
                                       "preferredcodec": "flac"}]
        ydl_opts["format"] = "bestaudio"
        
    return ydl_opts
