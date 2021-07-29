# Download the data, and send it to arduino

import urllib.request as url
import time
import serial

# create a serial object
ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)

cloud_api='https://api.thingspeak.com/channels/1458627/feeds.json?api_key=UCCHDI6UZBN76YFW&results=1' # read api >

while True:
 k=url.urlopen(cloud_api).read().decode('utf-8')
 k=k.split('"')[-2]
 print(k)
 if k=='on' or k=='ON':
  ser.write("on".encode('utf-8'))
 elif k=='off' or k=='OFF':
  ser.write("off".encode('utf-8'))
 time.sleep(2)
