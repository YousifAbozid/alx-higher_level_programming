#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbers = sys.argv
    length = len(numbers)
    result = 0
    for i in range(1, len(numbers)):
        result += int(numbers[i])
    print("{:d}".format(result))
