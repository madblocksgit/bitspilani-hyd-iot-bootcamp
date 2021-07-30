
from pymongo import MongoClient
dbclient=MongoClient('127.0.0.1',27017)

db=dbclient['bitsphyd']
c=db['dht11']

for i in c.find():
 print(i)
