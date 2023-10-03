#!/usr/bin/python3
for i in range(0, 10):
    for o in range(0, 10):
        if o != i and o > i:
            if o + i == 17:
                print("{:d}{:d}".format(i, o))
                break
            print("{:d}{:d}".format(i, o), end=", ")
