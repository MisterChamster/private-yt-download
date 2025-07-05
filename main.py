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
                 extract_plist_data,
                 ask_plist_action)



while True:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)
    print()
    url = ask_url()
    print()
    url_type = check_url_type(url)

    if url_type == 'plist':
        url_type = ask_plist_action()

        if url_type == 'download':
            print()
            save_plist(url)
        elif url_type == 'extract':
            print()
            extract_plist_data(url)

    elif url_type == "single":
        print()
        save_single(url)

    again = " "
    while again not in ["", "y", "e"]:
        again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
    if again == "e":
        print()
        break
