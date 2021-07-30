# sudo python3 rpi-button-led.py

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN) # BUTTON (OC - 1, CC - 0)
GPIO.setup(21, GPIO.OUT) # LED (0 - ON, 1 - OFF)


while True: # Infinite Loop
  if GPIO.input(2): # reading the data from GPIO2
    GPIO.output(21,1) # OFF
  else:
    GPIO.output(21,0) # ON
