from pymongo import MongoClient

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["films"]

fid=input('Enter film ID : ')
nm=input('Enter film name : ')
cat=input('Enter category : ')
yr=int(input('Enter release year : '))
ac=input('Enter actor : ')
acs=input('Enter actress : ')

dic={}
dic['_id']=fid
dic['filmnm']=nm
dic['category']=cat
dic['releaseyr']=yr
dic['actor']=ac
dic['actress']=acs

print(dic)

coll.insert_one(dic)
print('film document inserted to collection films')