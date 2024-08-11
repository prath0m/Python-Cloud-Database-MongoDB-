from pymongo import MongoClient
client = MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db = client["PrathamDB"]
coll = db["films"]

for doc in coll.find():
    print(doc)