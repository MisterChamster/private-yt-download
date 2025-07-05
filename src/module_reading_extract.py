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


def ask_round_or_exact():
    """
    Asks user if extracted video views should be exact or rounded.

    Returns:
        str: "round" or "exact".
    """
    input_RE = " "
    RE_dict = {"": "round", "r": "round", "e": "exact"}
    input_RE = input("Do You want viewcount on every video be exact or rounded? Extracting exact values will take significantly longer time. (Enter - rounded, e - exact)\n>>").lower()

    if input_RE in RE_dict:
        return RE_dict[input_RE]