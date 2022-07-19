#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as ne:
        print("Exception: ", file=sys.stderr, end="")
        print(ne, file=sys.stderr)
        return None
