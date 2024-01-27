#!/usr/bin/python3
"""
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    request = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(request) as c80:
        print(c80.read().decode('utf-8'))
