#!/usr/bin/python3
"""this module creates a student class"""


class Student:
    """this is the student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary repr of this instance"""
        return self.__dict__
