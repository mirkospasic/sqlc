#!/bin/bash

FILE=$1
TOKEN=$2

if [ $# -lt 2 ]; then
    echo "usage: $0 file_for_check your_token"
    exit 1
fi

echo "{\"event_type\": \"sqlav\", \"client_payload\": { \"text\": \"" > data.txt
./extract_function.py $FILE | sed -z 's/\n/\\n/g' | sed -z 's/\t/\\t/g' >> data.txt
echo "\", \"filename\": \"$FILE\"}}" >> data.txt

curl -H "Accept: application/vnd.github.everest-preview+json"     -H "Authorization: token $TOKEN"     --request POST     --data @data.txt     https://api.github.com/repos/mirkospasic/sqlc/dispatches

rm data.txt

