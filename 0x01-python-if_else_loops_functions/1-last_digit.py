#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = ((number * -1) % 10) * -1
to_print = "Last digit of %d is %d and is" % (number, last_digit)
if last_digit > 5:
    print(to_print, "greater than 5")
elif last_digit == 0:
    print(to_print, "0")
else:
    print(to_print, "less than 6 and not 0")
