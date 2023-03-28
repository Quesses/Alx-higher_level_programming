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

    @classmethod
    def size(self):
        """ returs the size of square

        Returns:
            size of square
        """

        return self.__size

    @classmethod
    def size(self, value):
        """ Setter, sets the size of square

        Args:
            value (int): size of square
        """

        self.__size = value

    def area(self):
        """ Calculates the area of the square

        Returns:
            area calculated
        """

        self.area = self.__size ** 2

        return self.area
