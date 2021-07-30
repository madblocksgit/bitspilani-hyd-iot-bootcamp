import BlynkLib
import time
import random 
BLYNK_AUTH='VlxyVKYg3gZ6ZYOPjNe2X39DTe84NN-r'

#intialize blynk
blynk=BlynkLib.Blynk(BLYNK_AUTH)
READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"


# register handler for virtual pin V11 reading
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    value=value[0]
    print(value)
    if int(value)==1:
	print("ON")
    else:
	print("OFF")
while True:
	blynk.run()
	blynk.virtual_write(1,random.randint(0,100))
	blynk.virtual_write(2,random.randint(0,100))
	time.sleep(2)
