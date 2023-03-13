#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    sum_xy = sum(map(lambda x: x[0] * x[1], my_list))
    sum_y = sum(map(lambda y: y[1], my_list))
    return sum_xy / sum_y
