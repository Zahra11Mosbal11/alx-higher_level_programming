#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_roman = 0
    for i in range(len(roman_string) - 1):
        if roman[roman_string[i]] < roman[roman_string[i + 1]]:
            total_roman -= roman[roman_string[i]]
        else:
            total_roman += roman[roman_string[i]]
    total_roman += roman[roman_string[-1]]
    return total_roman
