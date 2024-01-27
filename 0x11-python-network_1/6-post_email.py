#!/usr/bin/python3
"""
takes url
post data with given email.
"""
import requests
from sys import argv

if __name__ == "__main__":
    with requests.post(argv[1], data={'email': argv[2]}) as c80:
        print(c80.text)
