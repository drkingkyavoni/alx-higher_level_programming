#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, # and displays the body of the response
curl -s -L --request GET $1
