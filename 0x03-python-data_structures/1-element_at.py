#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    len_list = len(my_list)
    if idx > len_list - 1:
        return
    return (my_list[idx])
