#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    with requests.get('https://alx-intranet.hbtn.io/status') as c80:
        print("Body response:")
        print("\t- type: {}".format(type(c80.text)))
        print("\t- content: {}".format(c80.text))
