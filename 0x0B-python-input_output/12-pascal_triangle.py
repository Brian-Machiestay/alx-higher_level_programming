#!/usr/bin/python3
"""this module creates a pascal triangle"""


def pascal_triangle(n):
    """this function does the real work"""

    if n <= 0:
        return []
    sublist = [1]
    triangle = []

    adder = 0
    triangle.append([1])
    if n == 1:
        return triangle
    sublist = []
    counter = 1
    for b in triangle:
        for i in b:
            sublist.append(adder + i)
            adder = i
        sublist.append(1)
        triangle.append(sublist)
        if counter == n - 1:
            break
        counter = counter + 1
        adder = 0
        sublist = []
    return triangle
