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
