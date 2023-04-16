#!/usr/bin/python3
"""Defines a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square defines a square
    inherits from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """special method
        returns: [Square] (<id>) <x>/<y> - <size>
        """
        ret_str = "[Square] ({}) ".format(self.id)
        ret_xy = "{}/{} - ".format(self.x, self.y)
        ret_size = "{}".format(self.size)

        return (ret_str + ret_xy + ret_size)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        either no-keyword arguments or key-worded arguments
        """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for atr in range(len(args)):
                if list_atr[atr] == 'size':
                    setattr(self, 'width', args[atr])
                    setattr(self, 'height', args[atr])
                else:
                    setattr(self, list_atr[atr], args[atr])
        else:
            for key, val in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', val)
                    setattr(self, 'height', val)
                else:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of class Square"""
        list_atr = ['id', 'size', 'x', 'y']
        rec_dict = {}

        for atr in list_atr:
            if atr == 'size':
                rec_dict[atr] = getattr(self, 'width')
            else:
                rec_dict[atr] = getattr(self, atr)

        return rec_dict
