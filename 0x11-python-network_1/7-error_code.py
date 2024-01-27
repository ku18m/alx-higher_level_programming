#!/usr/bin/python3
"""
takes url
post data with given email.
"""
import requests
from sys import argv

if __name__ == "__main__":
    with requests.get(argv[1]) as c80:
        if c80.status_code >= 400:
            print('Error code: {}'.format(c80.status_code))
        else:
            print(c80.text)
