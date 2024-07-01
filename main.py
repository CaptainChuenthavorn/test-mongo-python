import pymongo
import sys

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
# db.drop_collection("inventory")
# db.inventory.insert_many(
#     [
#         {"item": "journal", "qty": 25, "tags": ["blank", "red"], "dim_cm": [14, 21]},
#         {"item": "notebook", "qty": 50, "tags": ["red", "blank"], "dim_cm": [14, 21]},
#         {
#             "item": "paper",
#             "qty": 100,
#             "tags": ["red", "blank", "plain"],
#             "dim_cm": [14, 21],
#         },
#         {"item": "planner", "qty": 75, "tags": ["blank", "red"], "dim_cm": [22.85, 30]},
#         {"item": "postcard", "qty": 45, "tags": ["blue"], "dim_cm": [10, 15.25]},
#     ]
# )

# cursor = db.inventory.find({})
# cursor = db.inventory.find({"status": "D"})
# print(list(cursor))
# cursor = db.inventory.find({})


# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
from bson.son import SON

db.inventory.insert_many(
    [
        {
            "item": "journal",
            "instock": [
                SON([("warehouse", "A"), ("qty", 5)]),
                SON([("warehouse", "C"), ("qty", 15)]),
            ],
        },
        {"item": "notebook", "instock": [SON([("warehouse", "C"), ("qty", 5)])]},
        {
            "item": "paper",
            "instock": [
                SON([("warehouse", "A"), ("qty", 60)]),
                SON([("warehouse", "B"), ("qty", 15)]),
            ],
        },
        {
            "item": "planner",
            "instock": [
                SON([("warehouse", "A"), ("qty", 40)]),
                SON([("warehouse", "B"), ("qty", 5)]),
            ],
        },
        {
            "item": "postcard",
            "instock": [
                SON([("warehouse", "B"), ("qty", 15)]),
                SON([("warehouse", "C"), ("qty", 35)]),
            ],
        },
    ]
)
# cursor = db.inventory.find({"size.h": {"$lt": 15}})
# cursor = db.inventory.find({"size.h": {"$lt": 15}, "size.uom": "in", "status": "D"})
cursor = db.inventory.find({"instock": SON([("warehouse", "A"), ("qty", 5)])})
# cursor = db.inventory.find({"size.uom": "cm"})
# cursor = db.inventory.find({"$or": [{"item": "postcard"}, {"qty": {"$lt": 30}}]})
for document in cursor:
    print(document)
