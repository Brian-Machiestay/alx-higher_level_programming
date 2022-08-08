#!/usr/bin/python3
"""checks if there is a
a particular string and inserts a text on next line
"""


def append_after(filename="", search_string="", new_string=""):
    """does the job"""
    lines = ""
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    with open(filename, "r", encoding="UTF-8") as f:
        count = 0
        for i in f:
            size = len(search_string)
            while size < len(i):
                if i[size - len(search_string): size] == search_string:
                    lines.insert(count + 1, new_string)
                    count = count + 1
                    break
                size = size + 1
            count = count + 1
    lines = "".join(lines)
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(lines)
