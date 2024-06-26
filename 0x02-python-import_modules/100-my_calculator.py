#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, mul, div, sub

    num_args = len(sys.argv) - 1
    operators = ['+', '-', '*', '/']
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if not sys.argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    op_chosen = op_dict.get(sys.argv[2])
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, op_chosen(a, b)))
