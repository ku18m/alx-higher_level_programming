#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the body of the response.
curl -sH "X-School-User-Id: 98" "$1"
