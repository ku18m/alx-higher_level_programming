#!/usr/bin/python3
def magic_string():
    magic_string.counter = 1 + getattr(magic_string, "counter", 0)
    return (("BestSchool, " * (magic_string.counter - 1)) + "BestSchool")
