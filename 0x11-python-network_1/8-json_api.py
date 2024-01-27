#!/usr/bin/python3
"""
takes url
post data with given email.
"""
import requests
from sys import argv

if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
