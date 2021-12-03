
from pymongo import MongoClient

client = MongoClient()

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
#	{"$unwind": "$tracks"},
		{"$match": {
			"$nor": [{"tracks": {"$exists": False}}, {"tracks": {"$size": 0}}]}
		},
		{
		"$project":{
			"_id": "$artist_id",
			"total_length": {"$sum": "$tracks.duration"},
			"artist_id": "$artist_id"
			}
		},
		{
		"$sort": {"artist_id": 1}
		}	
])

for i in result:
	print(i)
