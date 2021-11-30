from pymongo import MongoClient
import json

client = MongoClient()

db = client["A4dbNorm"]

# Deals with Artists
artists_collection = db["Artists"]

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

# Deals with Tracks 
tracks_collection = db["Tracks"]

with open("Tracks.json", "r") as read_file:
    tracks_data = json.load(read_file)

tracks_id = []
counter = 0

for document in tracks_data:
    tracks_id.append(document["_id"]["$oid"])
    del document["_id"]
    document["_id"] = tracks_id[counter]
    counter += 1

ret = tracks_collection.insert_many(tracks_data)