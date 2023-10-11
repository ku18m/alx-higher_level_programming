#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        inner = []
        for x in i:
            inner.append(x * x)
        new_matrix.append(inner)
    return new_matrix
