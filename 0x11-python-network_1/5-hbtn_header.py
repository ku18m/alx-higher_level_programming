#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status.
"""
import requests
from sys import argv

if __name__ == "__main__":
    with requests.get(argv[1]) as c80:
        print(c80.headers.get('X-Request-Id'))
