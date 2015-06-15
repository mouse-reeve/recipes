#!/bin/bash

file=$1
echo $file
dir=$( echo $file | sed -e 's/^json.\([a-z_]*\)\/.*.json/\1/' )
md_file=$( echo $file | sed -e 's/json\/.*\/\(.*\).json/\1.md/' )

mkdir markdown/$dir
python formatMarkdown.py "`cat $file`" > markdown/$dir/$md_file

