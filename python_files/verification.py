def verify_sensitivity(sens):
    """
    verifies if the input is a float
    :param sens: the sensitivity input
    :return: bool
    """
    try:
        float(sens)
        return True
    except ValueError:
        return False

def verify_pref(pref):
    """
    verifies if the input is "o" or "n"
    :param pref: a string input
    :return: bool
    """
    if pref == "o" or pref == "n":
        return True
    else:
        return False

def verify_pref_choice (pref_choice):
    """
    verifies if the input is "f" or "h"
    :param pref_choice: a string input
    :return: bool
    """
    if pref_choice == "f" or pref_choice == "h":
        return True
    else:
        return False