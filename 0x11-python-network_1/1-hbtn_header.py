#!/usr/bin/python3
""" A  script that takes in a URL, sends a request to the URL """
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()["X-Request-Id"])
