#!/usr/bin/env bash
# Script that takes in a URL as an argument,
# sends a GET request to the URL,
# and displays the body of the response

if [[ $# -lt 1 ]]; then
	echo "Usage: ./3-methods.sh host:port"
	exit 1
fi
# echo $1
curl -s -H 'X-School-User-Id: 98' $1
