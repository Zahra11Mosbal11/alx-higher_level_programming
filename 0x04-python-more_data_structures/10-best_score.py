#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    i = 0
    for x in a_dictionary:
        if i < a_dictionary[x]:
            i = a_dictionary[x]
    for y in a_dictionary:
        if i == a_dictionary[y]:
            return y
