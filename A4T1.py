from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient()

db = client["A4dbNorm"]

# Deals with Artists
artists_collection = db["Artists"]

with open("artists.json", "r") as read_file:
    artists_data = loads(read_file.read())

artists_collection.insert_many(artists_data)

# Deals with Tracks
tracks_collection = db["Tracks"]

with open("tracks.json", "r") as read_file:
    tracks_data = loads(read_file.read())

tracks_collection.insert_many(tracks_data)
