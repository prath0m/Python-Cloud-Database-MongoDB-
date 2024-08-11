import pandas
from pymongo import MongoClient


url="http://sohamspring.azurewebsites.net/api/players/all"

df=pandas.read_json(url)
#print(df)

data=df.to_dict(orient="records")


client=MongoClient("mongodb+srv://pratham:swisshy@prathamclus.l5pmia2.mongodb.net/?retryWrites=true&w=majority")
db=client["praffulldb"]
coll=db["players"]

coll.insert_many(data)
print('all players from Java REST API added to MonogDB')
