def ask_url():
    print("Enter URL: \n>> ", end="")
    url = str(input())
    if '&list=' in url:
        url = url[:url.find('&list=')]
    return url


def ask_plist_action():
    while True:
        print("Choose playlist option:" \
              "Enter - download" \
              "e     - extract playlist data\n>> ")
        action = str(input())

        if action not in ["", "e"]:
            print("Incorrect input.\n")
        elif action == "":
            return "download"
        elif action == "e":
            return "extract"


def check_url_type():
    url = str(input("Enter URL: \n>> "))
    if (len(url) > 34 and url[:34] == 'https://youtube.com/playlist?list='):
        inputDE = " "
        while inputDE not in ["", "d", "e"]:
            inputDE = input("What do You want to do with playlist? (Enter - download, e - extract playlist data)\n>>").lower()
        if inputDE == "e":
            return [url, "extract"]
        return [url, 'plist']

    elif (len(url) > 17 and url[:17] == 'https://youtu.be/') or \
         (len(url) > 29 and url[:29] == 'https://www.youtube.com/watch'):
        return [url, 'single']

    else:
        print("Invalid URL!\n")
        return [url, 'invalid']


def ask_save_ext():
    """
    Asks user for extension.

    In infinite loop, forces user to input either 4, 3 or f 
    to get proper extension.

    Returns:
        str: Extenstion chosen by user.
    """
    user_input = " "
    format_dict = {"4": "mp4", "3": "mp3", "f": "flac"}
    while user_input not in format_dict:
        user_input = input("What format do You want to save as? (4 - mp4, 3 - mp3, f - flac)\n>> ").lower()

    return format_dict[user_input]
