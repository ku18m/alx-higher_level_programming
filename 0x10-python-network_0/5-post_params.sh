#!/bin/bash
# Takes in a URL, sends a POST request to that URL, and displays the body of the response.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
