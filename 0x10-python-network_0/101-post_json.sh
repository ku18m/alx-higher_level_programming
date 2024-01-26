#!/bin/bash
# Takes in a URL, sends a POST request to that URL, and displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
