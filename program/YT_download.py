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
from socket import create_connection
from functions import (CharPolice,
                       DelDuplicatesFromListOfLists,
                       Dots,
                       GetUrlAndType,
                       IllegalToAscii,
                       IsInternetAvailable,
                       NameYourFile,
                       RoundOrExact,
                       ZerosAtBeginning)
from functions_readers import (ReadDelDuplicates,
                               ReadExtractWriteOrder,
                               ReadNumbered,
                               ReadNumOfTracks,
                               ReadSaveExtension,
                               ReadTrimLens)
from functions_downloading import (SaveSingle,
                                   SavePlist,
                                   ExtractPlistData)


desktop_path = path.join(path.expanduser("~"), "Desktop")
ydl_getdata = {'quiet': True,
               'extract_flat': True,
               'force_generic_extractor': True
              }

while True:
    chdir(desktop_path)
    url_and_type = GetUrlAndType()
    ydl_opts = {"quiet": True}

    if url_and_type[1] == "extract":
        ExtractPlistData(url_and_type[0])

    elif url_and_type[1] != "invalid":
        format = ReadSaveExtension()
        if format == "mp4":
            ydl_opts["merge_output_format"] = "mp4"
            ydl_opts["format"] = "bestvideo+bestaudio/best"
        elif format == "mp3":
            ydl_opts["postprocessors"] = [{  "key": "FFmpegExtractAudio",
                                             "preferredcodec": "mp3"}]
            ydl_opts["format"] = "bestaudio"
        elif format == "flac":
            ydl_opts["postprocessors"] = [{  "key": "FFmpegExtractAudio",
                                             "preferredcodec": "flac"}]
            ydl_opts["format"] = "bestaudio"

        if url_and_type[1] == "single":
            SaveSingle(url_and_type[0])
        elif url_and_type[1] == "plist":
            SavePlist(url_and_type[0])

    again = " "
    while again not in ["", "y", "e"]:
        again = input("\nWhat now? (Enter - run program again, e - end program)\n>>").lower()
    if again == "e":
        print()
        break