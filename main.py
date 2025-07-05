# The Jimi Hendrix Experience - "Voodoo Child" (live) video
# https://youtu.be/qFfnlYbFEiE?si=XRGMojQVJ1CFlsAu
# Shinji - Soulja boy video
# https://youtu.be/t5WoHi7Oyiw?si=X2tS0FStPcUQkMHQ
# Journey in Satchidananda playlist
# https://youtube.com/playlist?list=OLAK5uy_l61jyu2-HfVxbgW4KFUruUOjU56T0az-s&si=rcgIfaJ2cmolcBDT


import os
from src import (ask_url,
                 check_url_type,
                 save_single,
                 save_plist,
                 extract_plist_data)



while True:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)
    # url = ask_url()
    url_and_type = check_url_type()

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
