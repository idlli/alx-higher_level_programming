#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    result = sum(map(lambda x: x[0] * x[1], my_list))
    weights = sum(map(lambda x: x[1], my_list))
    if weights == 0:
        return 0
    result /= weights
    return result
