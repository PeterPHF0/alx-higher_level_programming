#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    print("{} ".format(len(sys.argv) - 1), end='')

    if len(sys.argv) - 1 == 0:
        print("arguments.")
    elif len(sys.argv) - 1 == 1:
        print("argument:")
    else:
        print("arguments:")

    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
