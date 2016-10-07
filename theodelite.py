import numpy
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)
cap.set(5,1)

while(True): #loop for live feed
	ret, img = cap.read() #read webcam
	cv2.imshow('raw', img) #testing
	#img =  img[240:241, 0:640] #crop to 1 line
	img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY ) #convert to greyscale
	ret, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY) #convert to binary
	
	display = cv2.cvtColor( img, cv2.COLOR_GRAY2BGR ) #testing
	
	cv2.rectangle(display,(95*0+75,479),(95*1+75,481),(255,0,0),1) #testing
	channel1 = numpy.mean(img[480, 95*0+75:95*1+75])
	if channel1 > 127:
		channel1 = '1'
	else:
		channel1 = '0'
	cv2.putText(display, channel1, (95*0+75,260),1,1,(255,0,0),2) #testing
	
	cv2.rectangle(display,(95*1+75,479),(95*2+75,481),(255,0,0),1) #testing
	channel2 = numpy.mean(img[480, 95*1+75:95*2+75])
	if channel2 > 127:
		channel2 = '1'
	else:
		channel2 = '0'
	cv2.putText(display, channel2, (95*1+75,260),1,1,(255,0,0),2) #testing
	
	cv2.rectangle(display,(95*2+75,479),(95*3+75,481),(255,0,0),1) #testing
	channel3 = numpy.mean(img[480, 95*2+75:95*3+75])
	if channel3 > 127:
		channel3 = '1'
	else:
		channel3 = '0'
	cv2.putText(display, channel3, (95*2+75,260),1,1,(255,0,0),2) #testing
	
	cv2.imshow('Binary', display) #testing
	
	cv2.waitKey(20) #add delay for camera

cap.release()
cv2.destroyAllWindows()
