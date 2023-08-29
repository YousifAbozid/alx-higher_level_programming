#!/usr/bin/python3
"""
1. Square with size
A class Square that defines a square
"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initializes the square size as private instance attribute"""
        self.__size = size
