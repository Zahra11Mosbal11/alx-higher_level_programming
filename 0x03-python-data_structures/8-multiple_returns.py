#!/usr/bin/python3
def multiple_returns(sentence):
    len_str  = len(sentence)
    first = sentence[0] if len_str > 0 else "None"
    tu = len_str, first
    return (tu)
