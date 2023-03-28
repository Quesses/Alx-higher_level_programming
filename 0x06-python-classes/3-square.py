#!/usr/bin/python3
"""Square class, learning classes and docstring style coding."""


class Square:
    """ Defines a Square by another class Suare."""

    def __init__(self, size=0):
        """
        Initialize the square with a size (private instantiation)
        Either default size 0 or specified size

        Args:
            size (int): integer value > 0.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("sixe must be >= 0")
        
        self.__size = size

    def area(self):
        """ Calculates the area of the square

        Returns:
            area calculated
        """

        return self.__size ** 2
