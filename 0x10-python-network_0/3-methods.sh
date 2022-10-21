#!/bin/bash
# returns the body of a status 200 response
curl -s -X -I OPTIONS "$1" | grep "Allow" | grep -o "G[A-Z]*"
