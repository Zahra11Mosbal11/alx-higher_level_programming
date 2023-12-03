#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first = None

    else:
        first = sentence[0:1]
    
    len_str  = len(sentence)
    tu = (len_str, first)
    return (tu)
