#!/bin/bash
#  script that sends a DELETE request to the URL passed as the first argument &  displays the body of the response
curl -s "$1" -X DELETE
