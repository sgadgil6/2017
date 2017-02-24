# Python script to detect a magnetic field using a hall effect sensor
# Hall Effect Sensor used: US5881LUA
# Listen on pin 3, when the south pole of a magnet is near the front of the sensor, pin 3 will go down to 0V
import Adafruit_BBIO.GPIO as GPIO 
import time 
import datetime 
 
 
print 'setup GPIO P8_10 as input' 
GPIO.setup("P8_10", GPIO.IN, pull_up_down = GPIO.PUD_UP) 
def sensorCallback1(channel) :  
	timestamp = time.time()    
	stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')  

	if GPIO.input("P8_10") == 0 :   
		print 'Magnet Detected ' + stamp     
 

def main() :

	GPIO.add_event_detect("P8_10", GPIO.FALLING, callback=sensorCallback1) 
 	
	try:   
		while True :    
			time.sleep(1)  
	except KeyboardInterrupt:   
		print 'in keyboard interrupt'    
	GPIO.cleanup() 
 
if __name__=='__main__':  
	main() 
 
