#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if c % 2 == 1:
        print("{}".format(chr(c - 32)), end="")
    else:
        print("{}".format(chr(c)), end="")
