#!/bin/bash

python add_ingredients.py ingredients
for file in $( ls json/* ); do
    python ingest.py $file
done
