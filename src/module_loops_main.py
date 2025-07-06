import os
from .module_askers_common import ask_url
from .module_big_routes import (save_single,
                                save_plist)
from .module_utils import determine_url_type



def main_loop():
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        print()
        print("=============================================================")
        print("=======================  Welcome to   =======================")
        print("======================= YT Downloader =======================")
        print("=============================================================\n")
        url = ask_url()
        if url == "exit":
            return
        url_type = determine_url_type(url)

        if url_type == 'plist':
            print()
            save_plist(url)
        elif url_type == "single":
            print()
            save_single(url)
