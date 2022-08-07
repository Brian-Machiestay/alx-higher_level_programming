#!/usr/bin/python3
"""this module creates a student class"""


class Student:
    """this is the student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary repr of this instance"""
        thisdict = dict()
        if type(attrs) is list:
            for i in list(self.__dict__):
                for j in attrs:
                    if i == j:
                        thisdict[j] = self.__dict__[i]
            return thisdict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reloads from json"""
        for i in list(self.__dict__):
            if i in list(json):
                self.__dict__[i] = json[i]
