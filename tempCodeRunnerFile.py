from pymongo import MongoClient

client = MongoClient("hostname", 27017)
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
