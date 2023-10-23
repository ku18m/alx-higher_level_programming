#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    len = 0
    new_list = []

    while len < list_length:
        try:
            result = my_list_1[len] / my_list_2[len]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        finally:
            new_list.append(result)
            len += 1

    return new_list
