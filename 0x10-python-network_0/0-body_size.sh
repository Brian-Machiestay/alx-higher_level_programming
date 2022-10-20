#!/bin/bash
# displays the value of a single header attr
url=$1
curl -s -I "$url" | grep "Content-Length" | grep -o -e "[0-9]*"
