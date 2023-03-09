#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv[1:])
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
        print(f"{num_args}: {argv[1]}")
    else:
        print(f"{num_args} arguments:")
        for x in range(1, (num_args + 1)):
            print(f"{x}: {argv[x]}")
