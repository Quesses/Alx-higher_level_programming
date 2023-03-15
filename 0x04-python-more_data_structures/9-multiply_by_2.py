#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary)
    new_dictionary = {}
    for x in keys:
        val = a_dictionary[x]
        new_dictionary[x] = val * 2
    return new_dictionary
