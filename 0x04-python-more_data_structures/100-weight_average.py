#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    num = sum(x * y for x, y in my_list)
    denm = sum(y for _, y in my_list)
    res = num / denm
    return res
