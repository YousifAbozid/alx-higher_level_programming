#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv

import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    args = HTTPBasicAuth(argv[1], argv[2])
    fetch_url = requests.get("https://api.github.com/user", auth=args)
    print(fetch_url.json().get("id"))
