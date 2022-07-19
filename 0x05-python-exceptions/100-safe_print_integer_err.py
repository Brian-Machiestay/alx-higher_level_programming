#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ne:
        print("Exception: ", file=sys.stderr, end="")
        print(ne, file=sys.stderr)
        return False
