#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]
    for tup in (tuple_a, tuple_b):
        if len(tup) >= 1:
            result[0] += tup[0]
        if len(tup) >= 2:
            result[1] += tup[1]
    return tuple(result)
