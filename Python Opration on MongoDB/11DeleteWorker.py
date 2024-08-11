from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["workers"]

# db.workers.updateOne({},{$set:{}})

wid=input('Enter worker ID : ')
qr={}
qr['_id']=wid

coll.delete_one(qr)

print('document deleted successfully')