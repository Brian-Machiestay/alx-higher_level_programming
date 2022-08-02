#!/usr/bin/python3
"""creates no more empty geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits a baseGeometry"""
    def __init__(self, width, height):
        """instantiates this object"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
