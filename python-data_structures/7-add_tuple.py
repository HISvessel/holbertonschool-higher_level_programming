#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    Tup_1 = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    Tup_2 = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    combined = zip(Tup_1, Tup_2)
    tuple_c = tuple(map(sum, combined))
    return tuple_c
