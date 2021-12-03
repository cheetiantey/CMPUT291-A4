from pymongo import MongoClient
import datetime

client = MongoClient()

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
		{"$unwind": "$tracks"},
		{"$match": 
				{"tracks.release_date": {"$gt": datetime.datetime(1950, 1, 1, 0, 0)}},	
		},
		{"$project": {
			"_id": 1,
			"name": "$name",
			"t_name": "$tracks.name",
			"t_release_date": "$tracks.release_date"
			}
		},
		{"$sort": {"t_release_date": 1}}
])

for i in result:
	print(i)

					
