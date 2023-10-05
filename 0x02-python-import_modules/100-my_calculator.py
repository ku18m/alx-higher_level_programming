#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    ops = ['+', '-', '*', '/']
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
    if op == '+':
        print("{:d} {} {:d} = {:d}".format(a, ops[0], b, add(a, b)))
    if op == '-':
        print("{:d} {} {:d} = {:d}".format(a, ops[1], b, sub(a, b)))
    if op == '*':
        print("{:d} {} {:d} = {:d}".format(a, ops[2], b, mul(a, b)))
    if op == '/':
        print("{:d} {} {:d} = {:d}".format(a, ops[3], b, div(a, b)))
