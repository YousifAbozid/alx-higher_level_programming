#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv
    length = len(sys.argv)
    if length > 1:
        if length == 2:
            print("{:d} argument:".format(length - 1))
        else:
            print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {}".format(i, arguments[i]))
    else:
        print("{} arguments.".format(length - 1))
