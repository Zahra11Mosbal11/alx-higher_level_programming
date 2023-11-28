#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            formatted_number = "{}".format("FizzBuzz")
        elif num % 3 == 0:
            formatted_number = "{}".format("Fizz")
        elif num % 5 == 0:
            formatted_number = "{}".format("Buzz")
        else:
            formatted_number = "{}".format(num)
        print("{} ".format(formatted_number), end="")
