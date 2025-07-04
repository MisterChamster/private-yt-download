# The Jimi Hendrix Experience - "Voodoo Child" (live) video
# https://youtu.be/qFfnlYbFEiE?si=XRGMojQVJ1CFlsAu
# Shinji - Soulja boy
# https://youtu.be/t5WoHi7Oyiw?si=X2tS0FStPcUQkMHQ
# Ramones - "Ramones" playlist
# https://youtube.com/playlist?list=PLBnJv6rImVe-LcbIsBXzIp6BpV6hqZnoO&si=jNymhDVGkVd3QHNn


from yt_dlp import YoutubeDL
from os import chdir, mkdir, path, listdir
from math import ceil
from datetime import date
from time import localtime, strftime
from src import (char_police,
                 del_duplicates_from_listoflists,
                 dots,
                 illegal_to_ascii,
                 is_internet_available,
                 name_your_file,
                 zeros_at_beginning,
                 ask_url_and_type,
                 ask_del_duplicates,
                 ask_extract_write_order,
                 ask_numbering,
                 ask_num_of_tracks,
                 ask_read_trim_lens,
                 ask_round_or_exact,
                 get_ydl_options,
                 save_single,
                 save_plist,
                 extract_plist_data)



while True:
    desktop_path = path.join(path.expanduser("~"), "Desktop")
    chdir(desktop_path)
    url_and_type = ask_url_and_type()

    if url_and_type[1] == "extract":
        extract_plist_data(url_and_type[0])

    elif url_and_type[1] in ["single", "plist"]:
        if url_and_type[1] == "single":
            save_single(url_and_type[0])
        elif url_and_type[1] == "plist":
            save_plist(url_and_type[0])

    again = " "
    while again not in ["", "y", "e"]:
        again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
    if again == "e":
        print()
        break
