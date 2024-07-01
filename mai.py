from pymongo import MongoClient
import json

try:
    # start example code here
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    # end example code here

    client.admin.command("ping")
    print("Connected successfully")

    # other application code
    # Create database and collection
    db = client["genshinRecommedation"]
    collection = db["artifacts"]

    # Insert JSON data from file

    # with open("genshin-artifacts.json") as file:
    #     data = json.load(file)
    #     print(type(data))
    #     collection.insert_many(data)
    # print("inserted data")
    query = {
        "$and": [
            {"setKey": "FragmentOfHarmonicWhimsy"},
            {"substats": {"$elemMatch": {"key": "eleMas"}}},
            {"substats": {"$elemMatch": {"key": "atk_"}}},
        ]
    }

    cursor = collection.find(query)
    for document in cursor:
        print(document)
        print("\n*******************\n")
    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)
