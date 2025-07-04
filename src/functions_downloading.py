from yt_dlp import YoutubeDL
from math import ceil
from datetime import date
from time import localtime, strftime
from socket import create_connection
from os import chdir, mkdir, path, listdir
from functions import (CharPolice,
                       DelDuplicatesFromListOfLists,
                       Dots,
                       IllegalToAscii,
                       IsInternetAvailable,
                       NameYourFile,
                       RoundOrExact,
                       ZerosAtBeginning)
from functions_readers import (ReadUrlAndType,
                               ReadDelDuplicates,
                               ReadExtractWriteOrder,
                               ReadNumbered,
                               ReadNumOfTracks,
                               ReadSaveExtension,
                               ReadTrimLens)


desktop_path = path.join(path.expanduser("~"), "Desktop")
ydl_getdata = {'quiet': True,
               'extract_flat': True,
               'force_generic_extractor': True
              }



