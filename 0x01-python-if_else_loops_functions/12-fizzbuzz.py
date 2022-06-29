#!/usr/bin/python3
def fizzbuzz():
    for w in range(1, 101):
        if w % 3 == 0 and w % 5 == 0:
            print("FizzBuzz ", end="")
        elif w % 3 == 0:
            print("Fizz ", end="")
        elif w % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(w), end="")
    print()
