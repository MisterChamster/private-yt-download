from yt_dlp import YoutubeDL
from os import chdir, mkdir, path, listdir
from math import ceil
from datetime import date
from time import localtime, strftime
from .module import (char_police,
                      del_duplicates_from_listoflists,
                      dots,
                      illegal_to_ascii,
                      is_internet_available,
                      name_your_file,
                      zeros_at_beginning,
                      get_ydl_options)
from .module_askers_extract import (ask_extract_write_order,
                                      ask_round_or_exact)
from .module_askers_playlist import (ask_del_duplicates,
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


def extract_plist_data(plist_url):
    """
    Extracts data from a playlist to a file.

    Downloads a playlist dictionary, asks for round or exact viewcount and write 
    order. Depending on viewcount options, either gets it for every video from 
    playlist dictionary or downloads it for every video separately. Then, creates
    a directory with playlist name on desktop if it doesn't exist and makes a file
    inside. Inside, puts playlist data, then data of every video in order
    established earlier. In the end, puts number of errors that have occurred 
    during the extract.

    Args:
        plist_url (str): url of a playlist.
    """
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
    dir_name = char_police(plist_title)
    if dir_name == "":
        dir_name = illegal_to_ascii(plist_title)
    dir_name += "_extracts"
    
    round_or_exact = ask_round_or_exact()
    write_order = ask_extract_write_order()
    if round_or_exact == "round":
        plist_list = [[el["url"], el["title"], el["view_count"]] for el in plist_dict['entries']]
    elif round_or_exact == "exact":
        plist_list = [[el["url"], el["title"]] for el in plist_dict['entries']] 
        try:
            for el in plist_list:
                with YoutubeDL(ydl_getdata) as ydl:
                    temp_vid_dict = ydl.extract_info(el[0], download=False)
                el.append(temp_vid_dict["view_count"])
        except:
            if not is_internet_available():
                print("Internet connection failed.\n\n")
                return
            else:
                print("Something went wrong")

    print("Data is extracted and it's almost time to write everything to a file")
    plist_len = plist_dict['playlist_count']

    if write_order == "asc":
        start_index = 0
        end_index   = plist_len
        first_quart = ceil(plist_len/4)
        third_quart = ceil((plist_len/4)*3)
        pop_index   = 0
    else:
        start_index = plist_len - 1
        end_index   = -1
        first_quart = ceil((plist_len/4)*3)
        third_quart = ceil(plist_len/4)
        pop_index   = -1

    halfway         = ceil(plist_len/2)
    quart_dict      = {first_quart: "One quarter down, three to go", halfway: "We're halfway there!", third_quart: "Just one more quarter..."}
    total_errors    = 0
    calendarium     = str(date.today())
    current_time    = strftime("%H:%M:%S", localtime())
    filename        = dir_name + "_extract_" + calendarium[:4] + calendarium[5:7] + calendarium[8:10] + current_time[:2] + current_time[3:5] + current_time[6:8] + write_order

    if not path.exists(desktop_path + "/" + dir_name):
        mkdir(dir_name)
    chdir(dir_name)

    with open(filename + ".txt", "w") as f:
        f.write(f"Playlist name: \t\t\t{plist_title}\n")
        f.write(f"Playlist's url:\t\t\t{plist_dict['original_url']}\n")
        f.write(f"Playlist's owner: \t\t{plist_dict['channel']}\n")
        f.write(f"Owner's URL: \t\t\t{plist_dict['channel_url']}\n")
        modified_date = plist_dict['modified_date']
        modified_date = modified_date[-2:] + "." + modified_date[4:6] + "." + modified_date[:4]
        f.write(f"Playlist last updated on: \t{modified_date}\n")
        f.write(f"Time of this data extract: \t{calendarium}, {current_time} \n")
        f.write(f"Playlist views so far: \t\t{dots(plist_dict['view_count'])}\n")
        f.write(f"Current playlist length: \t{plist_len}\n\n\n\n")
        print("Downloading...")
        
        for index in range(start_index, end_index, 1-2*(end_index==-1)):
            if index in quart_dict:
                print(quart_dict.pop(index))

            try:
                f.write(f"{index + 1}. {plist_list[pop_index][1]}\n")
                f.write(f"Views: {dots(plist_list[pop_index][2])}\n")
                f.write(f"{plist_list[pop_index][0]}\n\n") #URL
            except:
                total_errors += 1
                f.write(f"{plist_len - index}. An error has occurred when trying to download data of a video with URL: {plist_list[pop_index]}\n\n")
            plist_list.pop(pop_index)

        if total_errors == 0:
            f.write("\n\n\n\n\nNo errors have occurred during extraction")
        else:
            f.write(f"\n\n\n\n\nNumber of errors during extraction: {total_errors}")
    
    print("\n" + plist_title + " data has been successfully extracted to Your desktop!")
    if total_errors == 0:
        print("No errors have occurred during extraction")
    else:
        print(f"Number of errors during extraction: {total_errors}")
