import serial
import paho.mqtt.client as mqtt

client=mqtt.Client()

ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

while True:
 t=ser.readline()
 t=t.decode('utf-8')
 if(t.startswith('#')):
  t=t[:-2] # \r\n
  print(t)
  client.connect('broker.hivemq.com',1883)
  print('Broker Connected')
  client.publish('bits/dht11',t)
  print('Data sent to all my subscribers')
