#!/usr/bin/python3
def addR(roman_fig=""):
    if roman_fig == "I":
        return 1
    elif roman_fig == "V":
        return 5
    elif roman_fig == "X":
        return 10
    elif roman_fig == "L":
        return 50
    elif roman_fig == "C":
        return 100
    elif roman_fig == "D":
        return 500
    elif roman_fig == "M":
        return 1000


def roman_to_int(roman_string):
    if (roman_string is None or not isinstance(roman_string, str)):
        return 0
    roman_fig = 0
    strL = len(roman_string) - 1

    for x in range(len(roman_string)):
        if roman_string[x] in "IVXLCDM":
            if x != strL and addR(roman_string[x]) < addR(roman_string[x + 1]):
                roman_fig += addR(roman_string[x]) * -1
            else:
                roman_fig += addR(roman_string[x])
    return roman_fig
