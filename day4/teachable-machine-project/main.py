# Teachable Machine
# sudo pip3 install gtts
# sudo pip3 install playsound
# sudo pip3 install opencv-python
# sudo pip3 install tensorflow
# sudo pip3 install pillow

# Sign Language Recognition
# Created a ML Model using Teachable Machine
# mobileNet (Fast CNN - Neural Network)

import cv2
import numpy as np
from gtts import gTTS
import playsound
import time
import os
import tensorflow.keras
from PIL import Image,ImageOps

c1flag=0
c2flag=0
c3flag=0

def playaudio(t): # 'hi'
	language='en'
	m=gTTS(text=t,lang=language,slow=False)
	m.save('out.mp3')
	time.sleep(1)
	playsound.playsound('out.mp3')
	os.remove('out.mp3')
	print('Successfully played')

# load the model
model=tensorflow.keras.models.load_model('keras_model.h5')

def sign_language_classifier(a):
	global c1flag,c2flag,c3flag
	# pre-processing 
	data=np.ndarray(shape=(1,224,224,3),dtype=np.float32)

	# open the image
	image=Image.open(a) # all the pixel values
	# 240*240*3 >40k pixels

	# resize the image
	size=(224,224)
	image=ImageOps.fit(image,size,Image.ANTIALIAS)

	# convert this image into numpy array
	image_array=np.asarray(image)

	# pixel values (0 to 255) into a (0 to 2)
	# normailsation - (0 to 2, 0 to 1)
	normalise_image_array=(image_array.astype(np.float32)/127.0)-1

	data[0]=normalise_image_array
	prediction=model.predict(data)
	prediction=list(prediction[0]) # [0,1,2,3]
	max_prediction=max(prediction)
	index_max=prediction.index(max_prediction)

	if(index_max==0):
		print('Empty Gesture')
		c1flag=0
		c2flag=0
		c3flag=0
	elif(index_max==1 and c1flag==0 and c3flag==0):
		print('Like Gesture Found')
		playaudio('I like what you are talking about')
		c1flag=1
	elif(index_max==2 and c2flag==0):
		print('Dislike Gesture Found')
		playaudio('I dilike about your words')
		c2flag=1
	elif(index_max==3 and c3flag==0):
		print('Victory Gesture Found')
		playaudio('We won the match')
		c3flag=1


# Access the Camera
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,240)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

while True:
	result,frame=cam.read() # result is 1
	if result==1:
		cv2.imwrite('test.jpg',frame)
		sign_language_classifier('test.jpg')
		cv2.imshow('captured window',frame)

		key=cv2.waitKey(1)
		if key==ord('q'):
			break



