# publishing task 
# publisher - client, subscriber - client, broker - server
import paho.mqtt.client as mqtt

# create a client object
client=mqtt.Client()

# connect with broker
client.connect('broker.hivemq.com',1883) # host, port
print('Broker Connected')

# Publish the message
client.publish('bits/hyd',"Hi Hello, Madhu here!") # topic, msg
