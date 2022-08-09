#!/usr/bin/python3
"""this module creates a square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this class creates and square and subclasses a Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string repr of this rectangle"""
        string = "[{}] ({}) {}/{} - {}".\
            format("Square", self.id, self.x, self.y, self.width)
        return string

    @property
    def size(self):
        """returns the size"""
        return self.height

    @size.setter
    def size(self, size):
        """sets the size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """this updates the attributes of this square"""
        count = 0
        if args:
            for i in args:
                if count == 0:
                    self.id = i
                    count += 1
                    continue
                if count == 1:
                    self.size = i
                    count += 1
                    continue
                if count == 2:
                    self.x = i
                    count += 1
                    continue
                if count == 3:
                    self.y = i
                    count += 1
                    continue
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """returns the dictionary repr of this square"""
        thisdict = {'id': self.id, 'x': self.x,
                    'size': self.height, 'y': self.y}
        return thisdict
