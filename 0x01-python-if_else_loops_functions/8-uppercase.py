#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chr_code = ord(c)
        if chr_code >= 97 and chr_code <= 123:
            c = chr(chr_code - 32)
        print("{}".format(c), end="")
    print()
