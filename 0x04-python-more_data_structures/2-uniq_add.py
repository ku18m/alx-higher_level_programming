#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set(my_list)
    x = 0
    for i in result:
        x += i
    return x
