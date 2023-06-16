#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if roman_string is None or type(roman_string) is not str:
        return result
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous = 0
    for char in roman_string:
        if previous in (1, 10, 100) and digits[char] > previous:
            result -= 2 * previous
        result += (previous := digits[char])
    return result
