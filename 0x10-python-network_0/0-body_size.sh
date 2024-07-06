#!/usr/bin/bash
# Script that takes in a URL, sends a request to that URL, and # displays the size of the body of the response
curl -s --head $1 | grep -i content-length | awk 'BEGIN {FS=": "}; {print $2}'
