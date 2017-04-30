echo "Recipes
=========

Things for making and eating.

Tags:
$( jq '.tags | select (.) | .[]' json/*.json json/**/*.json | sort | uniq -c | sort -r | head -5 | while read line; do
    echo "- $line"
done )
" > README.md
