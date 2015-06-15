#!/bin/bash

rm -rf markdown/
mkdir markdown

for file in $( ls json/*/* ); do
    ./generateMarkdown.sh "$file"
done
