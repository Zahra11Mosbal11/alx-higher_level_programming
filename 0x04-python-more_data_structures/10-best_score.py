#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    i = 0
    x = None
    for xk, iv in a_dictionary.items():
        if iv > i:
            i = iv
            x = xk
    return x
