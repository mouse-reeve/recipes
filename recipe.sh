#!/bin/bash

title=$1
filename=$( echo $title | awk '{print tolower($0)}' | sed -e 's/ /_/g')'.json'

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
}" > json/$filename

vim json/$filename

./generateMarkdown.sh json/$filename
