#!/bin/bash

file=$1
echo $file
md_file=$( echo $file | sed -e 's/json\/\(.*\).json/\1.md/' )

source venv/bin/activate
python FormatMarkdown.py $file > markdown/$md_file
deactivate

