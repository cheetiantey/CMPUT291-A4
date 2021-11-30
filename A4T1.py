from pymongo import MongoClient
import json

client = MongoClient()

db = client["A4DBNorm"]

artists_collection = db["Artists"]
tracks_collection = db["Tracks"]

with open("test.json", "r") as read_file:
    artists_data = json.load(read_file)

artists_pk = []
counter = 0
# Extract the $oid to be used as "_id" in mongo
for document in artists_data:
    artists_pk.append(document["_id"]["$oid"])
    del document["_id"]
    document["_id"] = artists_pk[counter]
    counter += 1

# for i in range(len(artists_data)):   
#     print("Here") 
#     artists_data["_id"] = artists_pk[i]
    # print(artists_data["_id"])

# print(artists_data)




ret = artists_collection.insert_many(artists_data)
# print(data[0])