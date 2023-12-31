#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        try:
            div_lists = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_lists = 0
        except ZeroDivisionError:
            print("division by 0")
            div_lists = 0
        except IndexError:
            print("out of range")
            div_lists = 0
        finally:
            res.append(div_lists)
    return res
