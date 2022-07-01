#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5
print("{} + {} = {}".format(str(a), str(b), str(calc.add(a, b))))
print("{} - {} = {}".format(str(a), str(b), str(calc.sub(a, b))))
print("{} * {} = {}".format(str(a), str(b), str(calc.mul(a, b))))
print("{} / {} = {}".format(str(a), str(b), str(calc.div(a, b))))
