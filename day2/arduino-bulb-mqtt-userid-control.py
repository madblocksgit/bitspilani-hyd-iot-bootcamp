import paho.mqtt.client as mqtt
import serial

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)
client=mqtt.Client()
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

client.subscribe('bits/hyd')

def mummy(client,userdata,msg):
 t=msg.payload.decode('utf-8') # 1234,on
 t=t.split(',') # t[0] - 1234 t[1] - on
 print(t)
 if(t[0]=='7893015625' and t[1]=='on'):
  ser.write('on'.encode('utf-8'))
 elif(t[0]=='7893015625' and t[1]=='off'):
  ser.write('off'.encode('utf-8'))

client.on_message=mummy
client.loop_forever()
