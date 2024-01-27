#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
uses the GitHub API to display your id.
"""
import requests
import requests.auth
from sys import argv

if __name__ == "__main__":
    authentication = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=authentication)
    print(response.json().get("id"))
