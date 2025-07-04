def ask_extract_write_order():
    """
    Asks user for extract order.

    Returns:
        string: "asc" or "desc".
    """
    order = ""
    result_dict = {"a": "asc", "d": "desc"}
    while order not in result_dict:
        order = input("In what order do You want to write elements to file? (a - ascending, d - descending)\n>>").lower()
    return result_dict[order]
