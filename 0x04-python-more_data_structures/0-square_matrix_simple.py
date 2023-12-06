#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_mtx = list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
    return (new_mtx)
