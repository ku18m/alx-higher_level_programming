#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    name = None
    for key in a_dictionary:
        if a_dictionary.get(key) > int(best):
            best = a_dictionary.get(key)
            name = key
    return name
