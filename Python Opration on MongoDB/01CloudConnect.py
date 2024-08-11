#pip install pymongo

from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["workers"]

print('connected to MongoDB cloud successfully')

for doc in coll.find():
    print(doc)