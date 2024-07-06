#!/usr/bin/env bash
# Script that takes in a URL, sends a request to that URL, and
# displays the size of the body of the response

if [[ $# -ne 1 ]]; then
	echo "Usage: ./0-body_size.sh host:port"
	exit 1
fi
# curl -s --head $1 | grep -i content-length | awk -d: '{print $2}'
curl -s --head $1 | grep -i content-length | awk 'BEGIN {FS=": "}; {print $2}'
