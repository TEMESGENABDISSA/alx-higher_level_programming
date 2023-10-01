#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL &  displays"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
