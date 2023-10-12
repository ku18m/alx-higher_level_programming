#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_numeral = {"I": 1,
                     "V": 5,
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000}
    num = 0
    prev_c = "M"
    for c in roman_string:
        for key in roman_numeral.keys():
            if key == c:
                num += roman_numeral.get(key)
                if roman_numeral.get(prev_c) < roman_numeral.get(key):
                    num -= roman_numeral.get(prev_c) * 2
        prev_c = c
    return num
