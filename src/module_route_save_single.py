from yt_dlp import YoutubeDL
from os import path
from .module_askers_common import ask_save_ext
from .module_utils import (char_police,
                           illegal_to_ascii,
                           is_internet_available,
                           get_ydl_options)



def save_single(url):
    """
    Downloads element from given URL

    Extracts video title from URL, checks if it's correct, adjusts YoutubeDL 
    object parameters and downloads.

    Args:
        url (str) - correct URL to youtube video
    """
    extension = ask_save_ext()
    print()
    ydl_opts = get_ydl_options(extension)
    ydl_getdata = {'quiet': True,
                   'extract_flat': True,
                   'force_generic_extractor': True}
    desktop_path = path.join(path.expanduser("~"), "Desktop")

    try:
        with YoutubeDL(ydl_getdata) as ydl:
            og_title = ydl.extract_info(url, download=False)["title"]
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return

    finalname = char_police(og_title)
    if finalname == "":
        finalname = illegal_to_ascii(og_title)
    i = 1
    while path.exists(desktop_path + "/" + finalname):
        finalname += "_d"*i
        i += 1

    ydl_opts["outtmpl"] = finalname
    ydl_opts["paths"] = {"home": desktop_path}
    print("Downloading...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{finalname} has been successfully downloaded.\n\n")
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return
