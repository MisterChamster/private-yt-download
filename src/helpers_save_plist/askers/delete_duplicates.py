def ask_del_duplicates() -> bool:
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
