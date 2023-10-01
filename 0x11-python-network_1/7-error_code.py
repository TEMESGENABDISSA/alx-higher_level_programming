#!/usr/bin/python3
"""A script that Sends a request to a given URL and displays the response body:
-- The body of the response if there are no errors,
-- The error code when there is an HTTP error.."""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
