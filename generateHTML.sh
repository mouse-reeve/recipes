#!/bin/bash

file=$1
html_file=$( echo $file | sed -e 's/json\/\(.*\).json/\1.html/' )
mkdir -p html$( echo "/$html_file" | sed 's|/[^/]*$||' )

source venv/bin/activate
python3 format_file.py $file "html" > html/$html_file
deactivate
