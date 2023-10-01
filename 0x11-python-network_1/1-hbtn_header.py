#!/usr/bin/python3
"""A Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL> or value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()["X-Request-Id"])
