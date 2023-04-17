#!/usr/bin/python3
"""Defines a class Rectabgle"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle with inheritance from Base class

    Attributes:
        width : (int) width of the rectangle
        height : (int) height of the rectangle
        x : coordinate x
        y : coordinate y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ public method

        Returns:
            the area of the of the rectangle
        """
        area = self.__width * self.__height

        return area

    def display(self):
        """Public method
        prints in stdout the Rectangle instance with the character '#'
        """
        rectangle = '\n' * self.y

        for h in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ('#' * self.width) + '\n'
        print(rectangle, end="")

    def __str__(self):
        """special method
        returns: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        ret_str = "[Rectangle] ({}) ".format(self.id)
        ret_xy = "{}/{} - ".format(self.x, self.y)
        ret_wh = "{}/{}".format(self.width, self.height)

        return (ret_str + ret_xy + ret_wh)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        either no-keyword arguments or key-worded arguments
        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for atr in range(len(args)):
                setattr(self, list_atr[atr], args[atr])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """ Returns the dictionary representation of class Rectangle """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        rec_dict = {}

        for atr in list_atr:
            rec_dict[atr] = getattr(self, atr)

        return rec_dict
