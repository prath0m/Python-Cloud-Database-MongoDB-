from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["films"]

for doc in coll.find():
    try:
        print("%s | %s | %s" %(doc["filmnm"],doc["actor"],doc["actress"]))
    except:
        pass