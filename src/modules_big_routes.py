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
