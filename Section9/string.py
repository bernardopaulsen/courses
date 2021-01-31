"""
Description : Module with functions to be applied on strings.
Author      : Bernardo Paulsen
Version     : 0.0.1
"""


def find_all(string : str, sub : str) -> list:
    """
    Returns list with indexes of all ocurrencies of substring inside string.

    Params
    ------
    string : str
        Main string
    sub : str
        Substring to be found on main string.

    Returns
    -------
    indexes : list
        List of indexes of ocurrencies of substring inside main string
    """
    indexes = []
    find    = string.find(sub)
    while find != -1:
        indexes.append(find)
        find = string.find(sub,find+1)    
    return indexes

def remove_spaces(string : str) -> str:
    """
    Removes blank spaces from string.

    Params
    ------
    string : str
        Main string.
    
    Returns
    -------
    final : str
        Main string withou blank spaces.
    """
    return string.replace(' ','')

def equal(string1 : str, string2 : str) -> bool:
    """
    Checks if strings are equal, ignoring case

    Params
    ------
    string1 : str
        Fisrt string.
    string2 : str
        Second string.

    Returns
    -------
    is_equal : bool
        True if strings are equal.
    """
    if string1.lower() == string2.lower():
        return True
    else:
        return False