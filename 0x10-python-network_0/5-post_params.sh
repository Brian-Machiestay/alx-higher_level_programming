#!/bin/bash
# post parameters
curl -s -X POST -H "email: test@gmail.com; subject: I will always be here for PLD" "$1"
