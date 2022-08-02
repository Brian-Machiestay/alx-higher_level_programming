#!/usr/bin/python3
"""creates no more empty geometry"""


class BaseGeometry:
    """no more empty geometry"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
