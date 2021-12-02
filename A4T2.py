from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()

db = client["A4dbEmbed"]

artists_tracks_collection = db["ArtistsTracks"]

#Artists
with open("artists.json", "r") as read_file:
    artists_data = loads(read_file.read())


#Tracks
with open("tracks.json", "r") as read_file:
    tracks_data = loads(read_file.read())

tracks_dict = {}

for document in tracks_data:
    current_track_id = document["track_id"]
    tracks_dict[current_track_id] = document



for artist in artists_data:
	artist_tracks = artist["tracks"]

	#Swap track id with actual track data
	for i, current_track_id in enumerate(artist_tracks):
		current_track = tracks_dict[current_track_id]
		artist_tracks[i] = current_track



ret = artists_tracks_collection.insert_many(artists_data)




















































