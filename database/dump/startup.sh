#!/bin/bash

echo "Executing MongoImport"
cd /dump

mongoimport --uri "mongodb://mongo-mitiebot:27017/degalera" -c=sources --mode=upsert --upsertFields=alias,domain --file=degalera.sources.json --jsonArray