#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list[::-1]
    for i in reversed_list:
        print("{:d}".format(reversed_list[i]))


# Or you can use list.reverse() method then loop over it like normal.