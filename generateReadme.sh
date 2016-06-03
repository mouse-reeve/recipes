echo "Recipes
=========

Things for making and eating.

Tags:
$( jq '.tags | select (.) | .[]' json/* | sort | uniq -c | sort -r | head -5 | while read line; do
    echo "- $line"
done )

Common ingredients:
$( jq '.ingredients | select (.) | .[]' json/* | cut -d { -f2 | cut -d } -f1 | sort | uniq -c | sort -r | head | while read line; do
    echo "- $line"
done )
" > README.md
