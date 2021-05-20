#!/usr/bin/python3
"""This module defines the class Square"""


class Square():
    """Class Square has width and height"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Class constructor meant for a kwargs dict"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Fetches the perimeter of a Square object"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
