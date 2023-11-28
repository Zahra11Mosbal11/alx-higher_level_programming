#!/usr/bin/python3
for tens in range(0, 10):
    for ones in range(tens + 1, 10):
        if (tens * 10 + ones) == 89:
            print("{:02}".format(tens * 10 + ones))
        else:
            print("{:02}, ".format(tens* 10 + ones), end="")
