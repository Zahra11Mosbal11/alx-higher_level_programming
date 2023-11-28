#!/usr/bin/python3
def uppercase(string):
    string_new = ""
    for character in string:
        if 97 <= ord(character) <= 122:
            character = chr(ord(character) - 32)
        string_new += character
    print(string_new)
