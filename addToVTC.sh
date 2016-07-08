#!/bin/bash

file=$1
echo $file
html_file=$( echo $file | sed -e 's/json\/\(.*\).json/\1.html/' )
python generateHTML.py $file > ../veganteaparty.club/teaparty/recipe/$html_file
