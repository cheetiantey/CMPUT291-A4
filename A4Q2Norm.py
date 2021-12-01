from pymongo import MongoClient

client = MongoClient()

db = client["A4dbNorm"]

result = db.Tracks.aggregate([
    {"$match": {
        "track_id": { "$regex": '^70', "$options": 'i' }
        }
    },
    {
        "$group":{
            "_id": "null",
            "avg_danceability": {"$avg": "$danceability"}
        }
    },
    {
    "$project":{
        "_id": 0,
        "avg_danceability": 1
    }
    }
])

for i in result:
    print(i)