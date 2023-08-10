#!/usr/bin/python3
import sys

from calculator_1 import add, div, mul, sub

if __name__ == "__main__":
    length = len(sys.argv)
    argv = sys.argv
    result = 0
    if length == 4:
        if argv[2] == "+":
            result = add(int(argv[1]), int(argv[3]))
        elif argv[2] == "-":
            result = sub(int(argv[1]), int(argv[3]))
        elif argv[2] == "*":
            result = mul(int(argv[1]), int(argv[3]))
        elif argv[2] == "/":
            result = div(int(argv[1]), int(argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print(
            "{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2],
                                           int(argv[3]), result))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
