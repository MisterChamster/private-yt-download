# The Jimi Hendrix Experience - "Voodoo Child" (live) video
# https://youtu.be/qFfnlYbFEiE?si=XRGMojQVJ1CFlsAu
# Shinji - Soulja boy
# https://youtu.be/t5WoHi7Oyiw?si=X2tS0FStPcUQkMHQ
# Ramones - "Ramones" playlist
# https://youtube.com/playlist?list=PLBnJv6rImVe-LcbIsBXzIp6BpV6hqZnoO&si=jNymhDVGkVd3QHNn


from os import chdir, path
from src import (ask_url_and_type,
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
