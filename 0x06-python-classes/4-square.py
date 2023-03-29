#!/usr/bin/python3
"""Square class, learning classes and docstring style coding."""


class Square:
    """ Defines a Square by another class Suare."""

    def __init__(self, size=0):
        """
        Initialize the square with a size (private instantiation)
        Either default size 0 or specified size

        :param size: integer value (>= 0)
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self) -> int:
        """ returns the size of square

        :return: size of square
        """

        return self.__size

    @size.setter
    def size(self, value) -> None:
        """ Setter, sets the size of square

        @param: int size of square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self) -> int:
        """ Calculates the area of the square

        :return: area calculated
        """

        return self.__size ** 2
