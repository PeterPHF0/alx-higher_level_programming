#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, mul, div, sub

    num_args = len(sys.argv) - 1
    operators = ['+', '-', '*', '/']
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}

    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    if not sys.argv[2] in operators:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)

    op_chosen = op_dict.get(sys.argv[2])
    operand1 = int(sys.argv[1])
    operand2 = int(sys.argv[3])

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], op_chosen(operand1, operand2)))
