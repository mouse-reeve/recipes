echo "Recipes
=========

Things for making and eating.

Tags:
$( jq '.tags | select (.) | .[]' json/* | sort | uniq -c | sort -r | head -5 | while read line; do
    echo "- $line"
done )
" > README.md
