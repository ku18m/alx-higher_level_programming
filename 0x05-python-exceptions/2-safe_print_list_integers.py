#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    ints = 0

    while len < x:
        try:
            print("{:d}".format(my_list[len]), end="")
            ints += 1
        except (ValueError, TypeError):
            continue
        finally:
            len += 1

    print()
    return ints
