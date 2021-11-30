from pymongo import MongoClient
import json

client = MongoClient()

db = client["A4DBNorm"]

artists_collection = db["Artists"]
tracks_collection = db["Tracks"]

with open("Artists.json", "r") as read_file:
    artists_data = json.load(read_file)


artists_id = []
counter = 0

# Extract the $oid to be used as the new "_id"
# Delete the "_id" in each document
# Append a new extracted "_id" to each document
for document in artists_data:
    artists_id.append(document["_id"]["$oid"])
    del document["_id"]
    document["_id"] = artists_id[counter]
    counter += 1

ret = artists_collection.insert_many(artists_data)
