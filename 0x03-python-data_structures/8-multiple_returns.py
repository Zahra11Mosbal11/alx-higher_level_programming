#!/usr/bin/python3
def multiple_returns(sentence):
    len_str  = len(sentence)
    if len_str == 0:
        first = "None"

    else:
        first = sentence[0]
    
    tu = (len_str, first)
    return (tu)
