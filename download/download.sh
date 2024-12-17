#!/bin/bash

mkdir -p downloads

wget --no-check-certificate \
     --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
     --wait=1 \
     --random-wait \
     --limit-rate=200k \
     --directory-prefix=downloads \
     --input-file=urls.txt