#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    combined = zip(tuple_a, tuple_b)
    tuple_c = tuple(map(sum, combined))
    return tuple_c
