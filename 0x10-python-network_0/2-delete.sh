#!/usr/bin/env bash
# Script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response

if [[ $# -lt 1 ]]; then
	echo "Usage: ./2-delete.sh host:port"
	exit 1
fi
# echo $1
curl -s --request DELETE $1
