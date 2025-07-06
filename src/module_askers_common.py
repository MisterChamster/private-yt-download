def ask_url():
    print("Enter URL of YouTube video or playlist:\n" \
    "(to exit input 'exit')" \
    "\n>> ", end="")
    url = str(input())
    if '&list=' in url:
        url = url[:url.find('&list=')]
    return url


def ask_save_ext():
    """
    Asks user for extension.

    In infinite loop, forces user to input either 4, 3 or f
    to get proper extension.

    Returns:
        str: Extenstion chosen by user.
    """
    while True:
        print("Choose file format for saving:\n" \
        "4 - mp4\n" \
        "3 - mp3\n" \
        "f - flac\n>> ", end="")
        user_input = str(input())

        if user_input == "4":
            return "mp4"
        elif user_input == "3":
            return "mp3"
        elif user_input == "f":
            return "flac"
        else:
            print("Invalid input!\n")
