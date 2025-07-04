from yt_dlp import YoutubeDL
from os import chdir, mkdir, path, listdir
from math import ceil
from datetime import date
from time import localtime, strftime
from .modules import (char_police,
                      del_duplicates_from_listoflists,
                      dots,
                      illegal_to_ascii,
                      is_internet_available,
                      name_your_file,
                      zeros_at_beginning,
                      get_ydl_options)
from .modules_reading_common import (ask_url_and_type)
from .modules_reading_extract import (ask_extract_write_order,
                                      ask_round_or_exact)
from .modules_reading_playlist import (ask_del_duplicates,
                                       ask_num_of_tracks,
                                       ask_numbering,
                                       ask_read_trim_lens)



def save_single(url):
    """
    Downloads element from given URL

    Extracts video title from URL, checks if it's correct, adjusts YoutubeDL 
    object parameters and downloads.

    Args:
        url (str) - correct URL to youtube video
    """
    ydl_opts = get_ydl_options()
    ydl_getdata = {'quiet': True,
                   'extract_flat': True,
                   'force_generic_extractor': True}
    desktop_path = path.join(path.expanduser("~"), "Desktop")
    try:
        with YoutubeDL(ydl_getdata) as ydl:
            OGtitle = ydl.extract_info(url, download=False)["title"]
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
            return
        else:
            print("Something went wrong")

    finalname = char_police(OGtitle)
    if finalname == "":
        finalname = illegal_to_ascii(OGtitle)
    i = 1
    while path.exists(desktop_path + "/" + finalname):
        finalname += "_d"*i
        i += 1

    ydl_opts["outtmpl"] = finalname
    ydl_opts["paths"] = {"home": desktop_path}
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n" + finalname + " has been successfully downloaded")
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
            return
        else:
            print("Something went wrong")


def save_plist(plist_url): 
    """
    Downloads elements from a youtube playlist.

    Gets a list of all urls and their respective names from a playlist, handles
    duplicates, reads number of tracks, numbering method and cutting names of 
    files. Then, makes a directory on desktop and starts downloading them, 
    assigning correct names to every file.

    Args:
        plist_url (str): URL of downloaded playlist.
    """
    ydl_opts = get_ydl_options()
    ydl_getdata = {'quiet': True,
                   'extract_flat': True,
                   'force_generic_extractor': True}
    desktop_path = path.join(path.expanduser("~"), "Desktop")
    try:
        with YoutubeDL(ydl_getdata) as ydl:
            plist_dict = ydl.extract_info(plist_url, download=False)
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
            return
        else:
            print("Something went wrong")


    plist_title = plist_dict['title']
    print(plist_title)
    plist_list = [[el['url'], el['title']] for el in plist_dict['entries']] 

    plist_list_no_dupli = del_duplicates_from_listoflists(plist_list)
    if len(plist_list) != len(plist_list_no_dupli):
        if ask_del_duplicates():
            plist_list = plist_list_no_dupli

    plist_len = plist_dict['playlist_count']
    index_range = ask_num_of_tracks(plist_len)
    numbered = ask_numbering(index_range[0], index_range[1])
    if numbered[0] != "not":
        temp_filenum = numbered[1]
        if numbered[0] == "asc":
            last_num = index_range[0] + plist_len
        elif numbered[0] == "desc":
            last_num = index_range[0] - plist_len
    else:
        temp_filenum = ""

    namecut_list = ask_read_trim_lens()

    dir_name = char_police(plist_title)
    if dir_name == "":
        dir_name = illegal_to_ascii(plist_title)

    while path.exists(desktop_path + "/" + dir_name):
        dir_name += "_d"
    mkdir(dir_name)
    chdir(dir_name)
    total_errors = 0
    fileindex = ""
    ydl_opts["paths"] = {"home": desktop_path + "/" + dir_name}
    print("Downloading...")

    for index in range(index_range[0], index_range[1]):
        vid_url = plist_list[index][0]
        vid_OGname = plist_list[index][1]
        
        if numbered[0] != "not":
            fileindex = zeros_at_beginning(temp_filenum, last_num)
            
        finalfilename = name_your_file(vid_OGname, fileindex, namecut_list)

        while finalfilename in listdir():
            finalfilename += "_d"
        ydl_opts["outtmpl"] = finalfilename

        if numbered[0] == "asc":
            temp_filenum += 1
        elif numbered[0] == "desc":
            temp_filenum -= 1

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([vid_url])
            print(finalfilename)
        except:
            if not is_internet_available():
                print("Internet connection failed.\n\n")
                return
            else:
                total_errors += 1
                print(f"{finalfilename} could not be downloaded. Here's link to this video: {vid_url}")

    if total_errors == 0:
        print("\n" + plist_title + " playlist has been successfully downloaded")
    elif total_errors == 1:
        print("\n" + "Downloading " + plist_title + " didn't go smooth. There has been 1 exception")
    else:
        print("\n" + "Downloading " + plist_title + " didn't go smooth. There have been " + str(total_errors) + " exceptions")
