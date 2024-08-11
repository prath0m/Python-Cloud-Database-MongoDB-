from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["films"]

code=input("enter film code : ")
dic={}
dic["_id"]=code
print(dic)

for doc in coll.find(dic):
  print(doc)