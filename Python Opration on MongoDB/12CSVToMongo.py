from pymongo import MongoClient
import pandas

client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["cars"]

df=pandas.read_csv('cars.csv')
#print(df)
data=df.to_dict(orient="records")
print(data)

coll.insert_many(data)
print('data from csv dataset is stored in the mongodb collection')

