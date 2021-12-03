from pymongo import MongoClient

client = MongoClient()

db = client["A4dbNorm"]

result = db.Artists.aggregate([
		{"$lookup":
			{
			"from": "Tracks",
			"localField": "artist_id",
			"foreignField": "artist_ids",
			"as": "track_info"
				}
		},
		{
		"$project":{
			"_id": "$artist_id",
			"total_length": {"$sum": "$track_info.duration"},
			"artist_id": "$artist_id"
			}
		},
		{
		"$sort": {"artist_id": 1}
		}	
])

for i in result:
	print(i)

