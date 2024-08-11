from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["workers"]

# db.workers.updateOne({},{$set:{}})

wid=input('Enter worker ID : ')
qr={}
qr['_id']=wid

print(qr)

newsal=float(input('Enter new salary : '))
ch={}
ch['salary']=newsal
print(ch)

upd={'$set':ch}
print(upd)

coll.update_one(qr,upd)
print('worker salary updated')