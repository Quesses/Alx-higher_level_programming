#!/usr/bin/python3
"""Defines class Rectangle"""


class Rectangle:
    """Defines a class Rectangle by another class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Private intantialization of the rectangle
        Either specified width and height or default 0

        Args:
        width: (int) value must => 0
        height: (int) value must => 0

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width of the rectangle

        Returns:
            width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width size of the rectangle

        Args:
            value: (int) user value that must >= 0
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ returns the height of the rectangle

        Returns:
            height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ setter, sets the height of the rectangle

        Args:
            value: (int) user value that nust >= 0
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ public method

        Returns:
            the area of the of the rectangle
        """

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """public instance that returns the rectangle perimeter

        Returns:
            perimeter of the rectangle
        """

        if (self.__width == 0 or self.__height == 0):
            return 0
        per = (self.__width * 2) + (2 * self.__height)
        return per
