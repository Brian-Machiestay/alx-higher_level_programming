#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        j = a / b
    except Exception:
        j = None
    finally:
        print("Inside result: {}".format(j))
        return j
