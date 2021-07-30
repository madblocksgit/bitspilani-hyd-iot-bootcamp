# read the data from rpi through mqtt

import paho.mqtt.client as mqtt
from pymongo import MongoClient

# create a client object to access mongodb server
dbclient=MongoClient('127.0.0.1',27017)

# select the database
db=dbclient['bitsphyd']

# select the collection
c=db['dht11']

# create a client
client=mqtt.Client()

# connect with broker
client.connect('172.31.41.58',1883)
print ('Broker Connected')

# subscribe
client.subscribe('bits/dht11')

# create a notification
def notify(client,userdata,msg):
 t=(msg.payload).decode('utf-8')
 t=t.split(',')
 temp=float(t[0][1:]) # temp [#24.0]
 hum=float(t[1])
 print(temp,hum)
 k={} # creating an empty dict (json document)
 k['temp']=temp # {'temp': 24.0}
 k['hum']=hum # {'temp':24.0,'hum':45.0}
 c.insert_one(k) # finally mongodb database will be storing 
 print ('Data Stored')

# configure the notification
client.on_message=notify

# repeat forever
client.loop_forever()
