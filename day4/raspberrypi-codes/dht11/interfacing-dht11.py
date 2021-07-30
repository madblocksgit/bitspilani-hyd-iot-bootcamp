# sudo pip3 install Adafruit_DHT
# sudo python3 dht11-interfacing.py

import Adafruit_DHT
import time

k = None


while True:
  k = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 21)
  print(k)
  time.sleep(4)
