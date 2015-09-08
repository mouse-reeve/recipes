#!/bin/bash

file=$1
echo $file
md_file=$( echo $file | sed -e 's/json\/\(.*\).json/\1.md/' )

python FormatMarkdown.py "`cat $file`" > markdown/$md_file

