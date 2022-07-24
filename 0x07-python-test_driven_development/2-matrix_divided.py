#!/bin/usr/python3
"""this module divides a
a matrix and returns a new
matrix
"""


def matrix_divided(matrix, div):
    """this module divides
    the content of a list of lists
    of integers
    """
    new_Mat = []
    new_Mat_cont = []
    size = 0
    changingsize = 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        else:
            if size == 0:
                size = len(matrix[0])
            if len(i) != size:
                raise TypeError("Each row of the matrix must\
 have the same size")
            for j in i:
                if type(j) is not float and type(j) is not int:
                    raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                divide = round(j / div, 2)
                new_Mat_cont.append(divide)
            new_Mat.append(new_Mat_cont)
            new_Mat_cont = []
    return new_Mat
