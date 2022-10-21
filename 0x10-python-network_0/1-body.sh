#!/bin/bash
# returns the body of a status 200 response
if [ "$(curl -s -I "$1" | grep "HTTP" | grep -o -e "[0-9][0-9][0-9]")" -eq 200 ]; then curl -s -X GET "$1"; fi
