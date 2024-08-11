from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["workers"]

wid=input('Enter worker id : ')
nm=input('Enter name : ')
dp=input('Enter department : ')
po=input('Enter post : ')
loc=input('Enter location : ')
sal=float(input('Enter salary : '))

dic={}
dic['_id']=wid
dic['name']=nm
dic['dept']=dp
dic['post']=po
dic['location']=loc
dic['salary']=sal

print(dic)

coll.insert_one(dic)
print('document added to workers collection')