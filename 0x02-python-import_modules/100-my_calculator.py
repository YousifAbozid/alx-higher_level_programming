#!/usr/bin/python3
import sys

from calculator_1 import add, div, mul, sub

if __name__ == "__main__":
    length = len(sys.argv)
    argv = sys.argv
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    result = 0
    if length == 4:
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
