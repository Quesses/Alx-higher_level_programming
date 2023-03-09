#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argzs = len(argv[1:])
    result = 0
    if argzs == 0:
        print(f"{result}")
    elif argzs == 1:
        print(f"{int(argv[1])}")
    else:
        for x in range(1, (argzs + 1)):
            result += int(argv[x])
        print(f"{result}")
