import paho.mqtt.client as mqtt

client=mqtt.Client()
a=input('Enter UserID: ') # 123
while True:
  k=input('Enter message: ') # on
  client.connect('broker.hivemq.com',1883)
  print('Broker Connected')
  client.publish('bits/hyd',a+','+k) # 123,on
  print('Msg Sent')
