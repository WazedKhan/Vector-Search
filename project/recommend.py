import pymongo

from icecream import ic

client = pymongo.MongoClient("mongodb+srv://wazedkhan119399:7LRU8OS2BQv2N00U@cluster0.edtgmjj.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_mflix
collection = db.movies
results = collection.find().limit(5)

for result in results:
    ic(result)