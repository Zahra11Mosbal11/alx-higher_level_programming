#!/usr/bin/python3
"""find a peak"""


def find_peak(list_of_integers):
    """findApeak"""
    if not len(list_of_integers):
        return None
    else:
        return max(list_of_integers)
