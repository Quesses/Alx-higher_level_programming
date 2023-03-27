#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as x:
        stderr.write("Exception: {}\n".format(x))
        return None
    else:
        return result
