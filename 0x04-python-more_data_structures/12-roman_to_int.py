#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
             "D": 500, "M": 1000, "IX": 9, "IV": 4, "XL": 40,
             "XC": 90, "CD": 400, "CM": 900, "XL": 40, "XC": 90}
    if roman_string in list(roman):
        return roman[roman_string]
    count = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string):
            if roman_string[i: i+2] in list(roman):
                count = count + roman[roman_string[i: i+2]]
                i = i + 2
                continue
        if roman[roman_string[i]]:
            count = count + roman[roman_string[i]]
        i = i + 1
    return count
