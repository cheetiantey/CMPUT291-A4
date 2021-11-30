from pymongo import MongoClient
import json

client = MongoClient()

db = client["A4dbEmbed"]

artists_tracks_collection = db["ArtistsTracks"]

#Artists
with open("artists.json", "r") as read_file:
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



#Tracks
with open("tracks.json", "r") as read_file:
    tracks_data = json.load(read_file)

tracks_id = []
counter = 0
tracks_dict = {}

for document in tracks_data:
    tracks_id.append(document["_id"]["$oid"])
    del document["_id"]
    document["_id"] = tracks_id[counter]
    counter += 1

    current_track_id = document["track_id"]
    tracks_dict[current_track_id] = document


for artist in artists_data:
	artist_tracks = artist["tracks"]

	#Swap track id with actual track data
	for i, current_track_id in enumerate(artist_tracks):
		current_track = tracks_dict[current_track_id]
		artist_tracks[i] = current_track



ret = artists_tracks_collection.insert_many(artists_data)




















































