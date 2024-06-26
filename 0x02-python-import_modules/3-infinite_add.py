#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arg_num = len(sys.argv) - 1
    arg_sum = 0
    for i in range(arg_num):
        arg_sum += int(sys.argv[i+1])

    print(arg_sum)
