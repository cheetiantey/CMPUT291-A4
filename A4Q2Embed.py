from pymongo import MongoClient

client = MongoClient()

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
    {
      "$unwind" : "$tracks"
    },
    {"$match": {
        "tracks.track_id": { "$regex": '^70', "$options": 'i' }
        }
    },
    {
        "$group":{
            "_id": "null",
            "avg_danceability": {"$avg": "$tracks.danceability"}
        }
    },
    {
    "$project":{
        "_id": 1,
        "avg_danceability": 1
    }
    }
])

for i in result:
    print(i)