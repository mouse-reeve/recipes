#!/bin/bash

category=$1
title=$2
filename=$( echo "$category/$title" | awk '{print tolower($0)}' | sed -e 's/ /_/g' | sed -e 's/\/\//\//g')

if [ "$title" == "" ]
then
    exit
fi

echo "{
    \"title\": \"$title\",
    \"quantity\": \"\",
    \"preptime\": \"\",
    \"totaltime\": \"\",
    \"notes\": \"\",
    \"ingredients\": [
        \"\"
    ],
    \"steps\": [
        \"\"
    ],
    \"source\": \"\",
    \"tags\": [\"\"]
}" > $filename\.json

vim $filename\.json

./generateMarkdown.sh $filename\.json

git add $filename\.json  markdown
