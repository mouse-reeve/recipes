#!/bin/bash

rm -rf markdown/
mkdir markdown

for file in $( ls json/*.json json/**/*.json ); do
    echo $file
    ./generateMarkdown.sh "$file"
done
