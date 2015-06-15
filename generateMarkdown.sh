#!/bin/bash

rm -rf markdown/
mkdir markdown

files=$( ls json/*/* )
for file in $files; do
    dir=$( echo $file | sed -e 's/^json.\([a-z_]*\)\/.*.json/\1/' )
    mkdir markdown/$dir
    md_file=$( echo $file | sed -e 's/json\/.*\/\(.*\).json/\1.md/' )

    echo $file
    python formatMarkdown.py "`cat $file`" > markdown/$dir/$md_file
done
