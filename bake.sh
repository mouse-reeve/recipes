#!/bin/bash

file=$1
cp $file $file-temp
python last_made.py $file-temp | jq . | cat > $file
rm $file-temp
