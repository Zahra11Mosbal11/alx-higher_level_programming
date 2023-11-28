#!/usr/bin/python3
for char in range(90, 64, -1):
    if char % 2 == 0:
        to_print = chr(char).lower()
    else:
        to_print = chr(char)
    print("{}".format(to_print), end="")
