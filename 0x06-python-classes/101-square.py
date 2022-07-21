#!/usr/bin/python3
"""creates a square module and instantiates it"""


class Square:
    """the square class"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiates the size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    @property
    def position(self):
        """returns the postion"""
        return self.__position

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        self.__init__(value)

    @position.setter
    def position(self, value):
        """returns the position"""
        self.__init__(self.size, value)

    def __repr__(self):
        """print uses this"""
        thissize = self.__size
        thispos = self.__position
        string = ""
        if thissize == 0:
            string = "\n"
        else:
            if (thispos[1] != 0):
                string = string + "\n"*thispos[1]
            for i in range(0, thissize):
                if (thispos[0] != 0):
                    string = string + " "*thispos[0]
                for j in range(0, thissize):
                    string = string + "#"
                string = string + "\n"
        return string

    def my_print(self):
        """prints the square"""
        thissize = self.__size
        thispos = self.__position
        if thissize == 0:
            print()
        else:
            if (thispos[1] != 0):
                print("\n"*thispos[1], end="")
            for i in range(0, thissize):
                if (thispos[0] != 0):
                    print(" "*thispos[0], end="")
                for j in range(0, thissize):
                    print("#", end="")
                print()
