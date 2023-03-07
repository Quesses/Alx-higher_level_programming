#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0):
        begin_str = str[:n]
        end_str = str[(n + 1):]
        return (begin_str + end_str)
    else:
        return str
