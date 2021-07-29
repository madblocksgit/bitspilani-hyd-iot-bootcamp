# User (Participant) -> Thingspeak IoT Cloud -> Download -> RPi -> Arduino -> Relay -> Bulb

import urllib.request as url

cloud_api='https://api.thingspeak.com/update?api_key=FQURF1VPRATGB37O&field1='

while True:
  k=input('Enter message: ')
  if(k=='on' or k=='ON'):
    a=cloud_api+'on'
    t=url.urlopen(a)
    print(t)
  elif(k=='off' or k=='OFF'):
    a=cloud_api+'off'
    t=url.urlopen(a)
    print(t)
