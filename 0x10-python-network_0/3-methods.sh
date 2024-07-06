#!/usr/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -I $1 | grep -i allow | awk 'BEGIN {FS=": "}; {print $2}'
