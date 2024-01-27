#!/usr/bin/python3
"""
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as c80:
            print(c80.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
