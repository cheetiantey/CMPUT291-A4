
from pymongo import MongoClient

client = MongoClient()

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
#		{"$match": {
#			"artist_id": {"$exists": True}
#			}
#		},
#		{"$unwind": "$tracks"},	
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
