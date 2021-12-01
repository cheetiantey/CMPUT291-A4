from pymongo import MongoClient

client = MongoClient()

db = client["A4dbNorm"]

result = db.Artists.aggregate([
    {"$match": {
        "$nor": [{"tracks": {"$exists": False}}, {"tracks": {"$size": 0}}]}
    },
    {"$project": 
        {"_id": 0,
         "artist_id": 1,
         "name": 1,
        "num_tracks" : { 
            "$cond": { "if": {"$isArray": "$tracks" }, "then" :{ "$size": "$tracks"}, "else": "0"} }
        }
    }
])

for i in result:
    print(i)