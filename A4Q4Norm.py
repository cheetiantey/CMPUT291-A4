import datetime

from pymongo import MongoClient

client = MongoClient()

db = client["A4dbNorm"]

result = db.Tracks.aggregate([
		{"$match": {
			"release_date": {"$gt": datetime.datetime(1950, 1, 1, 0, 0)}
			}
		},
		{"$lookup":
			{
			"from": "Artists",
			"localField": "artist_ids",
			"foreignField": "artist_id",
			"as": "track_info"
				}
		},
		{"$unwind": "$track_info"},
		{"$project":{
			"_id": "$track_info._id",
			"name": "$track_info.name",
			"t_name": "$name",
			"t_release_date": "$release_date"
			}
		},
		{"$sort": {"t_release_date": 1}}
])

for i in result:
	print(i)



