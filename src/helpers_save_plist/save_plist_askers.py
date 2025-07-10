def ask_del_duplicates():
    user_input = " "
    while True:
        print("Duplicates detected. Choose handling option:\n" \
              "d - Delete duplicates\n" \
              "l - Leave duplicates\n>> ", end="")
        user_input = str(input())

        if user_input == "d":
            return True
        elif user_input == "l":
            return False


def ask_read_trim_lens():
    """
    Asks user about cutting names of the elements.

    Returns:
        list[a, b]:
            a (int): Number of letters cut from the start of filename.
            b (int): Number of letters cut from the end of filename.
    """
    inputSC = " "
    namecut_list = [0, 0]
    while inputSC not in ["", "s", "b", "e"]:
        print("Choose name trimming option:\n" \
              "Enter - No trimming\n" \
              "s     - Trim at the start\n" \
              "e     - Trim at the end\n" \
              "b     - Trim on both sides\n>> ", end="")
        inputSC = str(input())

    if inputSC == "s":
        namecut_list[0] = str(input("Input the string or length You want to trim at the start:\n>>"))
        if namecut_list[0].isdigit():
            namecut_list[0] = int(namecut_list[0])
        else:
            namecut_list[0] = len(namecut_list[0])

    elif inputSC == "e":
        namecut_list[1] = str(input("Input the string or length You want to trim at the ending:\n>>"))
        if namecut_list[1].isdigit():
            namecut_list[1] = int(namecut_list[1])
        else:
            namecut_list[1] = len(namecut_list[1])

    elif inputSC == "b":
        namecut_list[0] = str(input("Input the string or length You want to trim at the start:\n>>"))
        if namecut_list[0].isdigit():
            namecut_list[0] = int(namecut_list[0])
        else:
            namecut_list[0] = len(namecut_list[0])

        namecut_list[1] = str(input("Input the string or length You want to trim at the ending:\n>>"))
        if namecut_list[1].isdigit():
            namecut_list[1] = int(namecut_list[1])
        else:
            namecut_list[1] = len(namecut_list[1])

    return namecut_list
