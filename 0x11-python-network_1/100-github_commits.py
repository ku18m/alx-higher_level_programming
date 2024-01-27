#!/usr/bin/python3
"""
takes your GitHub credentials (repo name and owner name)
uses the GitHub API to display commits.
"""
import requests
import requests.auth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
