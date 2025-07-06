import os
from .module_askers_common import ask_url
from .module_route_save_single import save_single
from .module_route_save_plist import save_plist
from .module_utils import determine_url_type



def main_loop():
    print()
    while True:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
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
