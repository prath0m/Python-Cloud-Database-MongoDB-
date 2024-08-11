from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["films"]

# db.films.updateOne({},{$set:{}})

fid=input('Enter film ID : ')
qr={}
qr['_id']=fid

newcol=float(input('Enter new collection : '))
ch={}
ch['collectionmn']=newcol

upd={'$set':ch}

coll.update_one(qr,upd)
print('film collection updated...')

print(qr)
print(upd)
