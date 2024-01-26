#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the allowed methods.
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
