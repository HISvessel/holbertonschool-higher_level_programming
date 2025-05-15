#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row = " ".join(map(str, row))
        print("{:d}".format(row))
