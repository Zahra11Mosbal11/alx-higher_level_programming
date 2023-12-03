#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return
    new_list = my_list
    if not (idx < 0 or idx >= len(my_list)):
        del new_list[idx]

    return (my_list)
