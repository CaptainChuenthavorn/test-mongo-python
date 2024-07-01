from pymongo import MongoClient

try:
    # start example code here
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    # end example code here

    client.admin.command("ping")
    print("Connected successfully")

    # other application code

    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)

db = client.genshin
collection = db.artifacts
collection.insert_one(
    {
        "setKey": "FragmentOfHarmonicWhimsy",
        "slotKey": "flower",
        "rarity": 5,
        "mainStatKey": "hp",
        "level": 20,
        "substats": [
            {"key": "critDMG_", "value": 17.1},
            {"key": "atk", "value": 29.0},
            {"key": "atk_", "value": 10.5},
            {"key": "eleMas", "value": 16.0},
        ],
        "location": "Arlecchino",
        "lock": False,
        "id": 0,
    }
)
# collection.find_one({"name": "name1"})
cursor = collection.find_one({"setKey": "FragmentOfHarmonicWhimsy"})
print(list[cursor])
