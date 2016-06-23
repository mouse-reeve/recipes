#!/bin/bash

title=$1
filename=$( echo $title | awk '{print tolower($0)}' | sed -e 's/ /_/g')

echo "{
    \"title\": \"$title\",
    \"notes\": \"\",
    \"ingredients\": [
        \"\"
    ],
    \"steps\": [
        \"\"
    ],
    \"source\": \"\",
    \"tags\": [\"\"]
}" > json/$filename\.json

vim json/$filename\.json

./generateMarkdown.sh json/$filename\.json

git add json/$filename\.json  markdown/$filename\.md
