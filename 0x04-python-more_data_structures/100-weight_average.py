#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0.0
    div_1 = 0.0
    div_2 = 0.0
    for k in my_list:
        div_1 += k[0] * k[1]
        div_2 += k[1]
    average = div_1 / div_2
    return average
