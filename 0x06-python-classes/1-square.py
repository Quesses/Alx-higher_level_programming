#!/usr/bin/python3
"""Square class, learning classes and docstring style coding."""


class Square:
    """ Defines a Square by another class Suare."""

    def __init__(self, size=None):
        """
        Initialize the square with a size (private instantiation)
        No type / value verification
        """

        self.__size = size
