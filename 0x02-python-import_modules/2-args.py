#!/usr/bin/python3

if __name__ == '__main__':

    print("{} ".format(len(argv)), end='')
    if len(argv) == 0:
        print("arguments.", end='')
    elif len(argv) == 1:
        print("argument:")
    else:
        print("arguments:")

    for i in range(len(argv)):
        print("{}: {}".format(i+1, argv[i+1]))
