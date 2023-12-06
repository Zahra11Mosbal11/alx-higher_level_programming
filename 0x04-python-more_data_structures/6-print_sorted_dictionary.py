#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary)
    for x in sorted_dictionary:
        value = a_dictionary[x]
        print("{:s}: {}".format(x, value))
