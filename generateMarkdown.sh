#!/bin/bash

file=$1
md_file=$( echo $file | sed -e 's/json\/\(.*\).json/\1.md/' )
mkdir -p markdown$( echo "/$md_file" | sed 's|/[^/]*$||' )

source venv/bin/activate
python FormatMarkdown.py $file > markdown/$md_file
deactivate

