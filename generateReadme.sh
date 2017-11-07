#!/bin/bash

echo "Recipes
=========

Things for making and eating.

To find a recipe to use, go to the [markdown directory](https://github.com/mouse-reeve/recipes/tree/master/markdown). For complaints, requests, or opinions, file an issue.

Tags:
$( jq '.tags | select (.) | .[]' json/**/*.json | sort | uniq -c | sort -r | head -5 | while read line; do
    echo "- $line"
done )
" > README.md
