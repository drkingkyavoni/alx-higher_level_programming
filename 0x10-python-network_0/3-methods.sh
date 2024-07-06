#!/usr/bin/env bash
# Script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response

if [[ $# -lt 1 ]]; then
	echo "Usage: ./3-methods.sh host:port"
	exit 1
fi
# echo $1
# curl -s --head $1 | grep -i allow | awk -d: '{print $2}'
curl -s -I $1 | grep -i allow | awk 'BEGIN {FS=": "}; {print $2}'
