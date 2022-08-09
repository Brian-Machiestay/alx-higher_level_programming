#!/usr/bin/python3
"""this module creates a rectangle"""


from models.base import Base


class Rectangle(Base):
    """this class creates a rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the Rectangle constructor"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """changes the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """changes the height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """changes the x value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """changes the y value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of this rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays this rectangle"""
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            if i < self.__height:
                print()

    def __str__(self):
        """returns a string repr of this rectangle"""
        string = "[{}] ({}) {}/{} - {}/{}".\
            format("Rectangle", self.id, self.__x, self.__y,
                   self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        count = 0
        if args:
            for i in args:
                if count == 0:
                    self.id = i
                    count += 1
                    continue
                if count == 1:
                    self.width = i
                    count += 1
                    continue
                if count == 2:
                    self.height = i
                    count += 1
                    continue
                if count == 3:
                    self.x = i
                    count += 1
                    continue
                if count == 4:
                    self.y = i
                    count += 1
                    continue
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dict repr of this rectangle"""
        thisdict = {'x': self.x, 'y': self.y, 'id': self.id,
                    'height': self.height, 'width': self.width}
        return thisdict
