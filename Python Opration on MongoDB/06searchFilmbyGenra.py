from pymongo import MongoClient
client = MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db = client["PrathamDB"]
coll = db["films"]

genre=input("Enter genre : ")
dic={}
dic["category"]=genre
print(dic)

for doc in coll.find(dic):
  print(doc)