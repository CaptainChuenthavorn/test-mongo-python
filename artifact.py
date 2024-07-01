import pymongo
import sys
import json

# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.

try:
    client = pymongo.MongoClient(
        "mongodb+srv://admin:admin@cluster0.e1hu4of.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )

# return a friendly error if a URI error is thrown
except pymongo.errors.ConfigurationError:
    print(
        "An Invalid URI host error was received. Is your Atlas host name correct in your connection string?"
    )
    sys.exit(1)

# use a database named "myDatabase"
db = client.myDatabase
collection_currency = db["artifacts"]
# with open("genshin-artifact-data.json") as f:
#     file_data = json.load(f)
# print(type(file_data))
# collection_currency.insert_one(file_data)

cursor = collection_currency.find({"setKey": "GoldenTroupe"})
for document in cursor:
    print(document)
# print(len(list[cursor]))
