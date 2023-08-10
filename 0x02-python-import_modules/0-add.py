#!/usr/bin/python3
from add_0 import add

# Here is empty code so when you import this module into another module
# the global variable __name__ is "__this_module_name_itself__"
# so it prints nothing

if __name__ == "__main__":
    # When you run this module directly like ./0-add.py or python3 0-add.py
    # the global variable __name__ is "__main__"
    # then this module is executed as a script
    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
