#!/usr/bin/python3
for number in range(0, 100):
    if number <= 9:
        formatted_number = "{:02}, ".format(number)
    elif number == 99:
        formatted_number = "{}\n".format(number)
    else:
        formatted_number = "{}, ".format(number)
    print("{}".format(formatted_number), end="")

