from yt_dlp import YoutubeDL
from src.common.utils import is_internet_available



def get_video_title(url):
    ydl_getdata = {'quiet': True,
                   'extract_flat': True,
                   'force_generic_extractor': True}
    
    try:
        with YoutubeDL(ydl_getdata) as ydl:
            og_title = ydl.extract_info(url, download=False)["title"]
            return og_title
    except:
        if not is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return "Error"
