#!/usr/bin/python3
"""LockedClass Module"""


class LockedClass:
    """
    A class with no class or object attribute
    that prevents the user from dynamically creating new instance attribute
    """

    __slots__ = ["first_name"]

    def __init__(self):
        pass
