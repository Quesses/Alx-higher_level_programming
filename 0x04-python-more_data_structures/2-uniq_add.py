#!/usr/bin/python3
def uniq_add(my_list=[]):
    s_list = set(my_list)
    result = 0
    for x in s_list:
        result += x
    return result
