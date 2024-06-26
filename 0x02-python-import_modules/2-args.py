#!/usr/bin/python3

if __name__ == '__main__':

    print("{} ".format(len(argv) - 1), end='')
    if len(argv) - 1 == 0:
        print("arguments.", end='')
    elif len(argv) - 1 == 1:
        print("argument:")
    else:
        print("arguments:")

    for i in range(len(argv) - 1):
        print("{}: {}".format(i+1, argv[i+1]))
