def ask_trim_names_main_menu():
    while True:
        print("Choose element name trimming option:\n" \
              "tas - Trim all names at the start...\n" \
              "tae - Trim all names at the end...\n" \
              "tre - Trim a range of elements... \n" \
              "tsv - Trim specific tracks by value...\n" \
              "s   - Save\n>> ", end="")
        asker = str(input())

        if asker not in ["tas", "tae", "tre", "tsv", "s"]:
            print("Incorrect input.\n")
        else:
            return asker
