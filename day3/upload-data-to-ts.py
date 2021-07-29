# DHT11 -> Arduino -> RPi (USB) - Pub -> MQTT Broker -> Sub (Google Colab)

import paho.mqtt.client as mqtt
import urllib.request as url

cloud_api='https://api.thingspeak.com/update?api_key=ZX82MU67SO1M5JHJ&field1='
# create a client object
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

# Subscribe
client.subscribe('bits/dht11')

# create a notification function
def notify(client,userdata,msg):
  global cloud_api
  t=msg.payload.decode('utf-8') # string
  t=t.split(',') # list of strings
  #print(t)
  temp=float(t[0][1:])
  hum=float(t[1])
  print("Temp: {0}".format(temp));
  print("Hum: {0}".format(hum))
  cloud_api=cloud_api+str(temp)+'&field2='+str(hum)
  k=url.urlopen(cloud_api)
  print(k)

# configure this notify
client.on_message=notify
client.loop_forever()
