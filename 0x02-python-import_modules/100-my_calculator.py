#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    _, a, op, b = argv
    a = int(a)
    b = int(b)
    op_dict = {'+': add, '-': sub, '*': mul, '/': div}
    if op not in op_dict:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print(f'{a} {op} {b} = {op_dict[op](a, b)}')
