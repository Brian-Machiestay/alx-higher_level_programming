#!/bin/bash
# displays the value of a single header attr
curl -s -I "$1" | grep "Content-Length" | grep -o -e "[0-9]*"
