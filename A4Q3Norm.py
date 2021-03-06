from pymongo import MongoClient

client = MongoClient()

db = client["A4dbNorm"]

result = db.Tracks.aggregate([
		{"$unwind": "$artist_ids"
		 },
		{"$group": {
			"_id": "$artist_ids",
			"total_length": {"$sum": "$duration"}
			}
		},
		{
		"$project":{
			"_id": 1,
			"artist_id": "$_id",
			"total_length": 1
			}
		},
		{
		"$sort": {"artist_id": 1}
		}


])

for i in result:
	print(i)
