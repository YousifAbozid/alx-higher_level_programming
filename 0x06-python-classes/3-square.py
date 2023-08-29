#!/usr/bin/python3
"""
3. Area of a square
A class Square that defines a square
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initializes the square size as private instance attribute
        Raise TypeError & ValueError if not int or <0 resp.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size**2
