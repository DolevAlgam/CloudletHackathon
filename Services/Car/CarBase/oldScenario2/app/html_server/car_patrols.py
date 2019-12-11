import time
import requests
import sts

def scanSuspect():
	#r = requests.get('http://jetson:5000/scan')
	time.sleep(2)
        if True:
                sts.setSpeed(100)
                sts.forward()
                time.sleep(2)
                sts.stop()
		time.sleep(1)

def scenario2():
	sts.forward()
	time.sleep(5)
	sts.stop()
	scanSuspect()
	sts.backward()
	time.sleep(5)
	sts.stop()
