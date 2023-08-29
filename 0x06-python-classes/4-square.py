#!/usr/bin/python3
"""
4. Access and update private attribute
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

    @property
    def size(self):
        """Returns the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
