#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    no = len(sys.argv)
    op = "+-*/"
    if no != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = sys.argv[2]
    if c == "+":
        print("{} {} {} = {}".format(a, c, b, calc.add(a, b)))
    elif c == "-":
        print("{} {} {} = {}".format(a, c, b, calc.sub(a, b)))
    elif c == "*":
        print("{} {} {} = {}".format(a, c, b, calc.mul(a, b)))
    elif c == "/":
        print("{} {} {} = {}".format(a, c, b, calc.div(a, b)))
