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

def sectionA():
	sts.forward()
	time.sleep(4)
	sts.turnRight()
	time.sleep(1)
	sts.forward()
	time.sleep(3)
	sts.stop()
	scanSuspect()
        sts.backward()
        time.sleep(5)
	sts.turnLeft()
	time.sleep(1)
	sts.backward()
	time.sleep(4)
        sts.stop()

def sectionB():
	sts.forward()
        time.sleep(2)
        sts.turnLeft()
        time.sleep(1)
        sts.forward()
        time.sleep(6)
        sts.stop()
        scanSuspect()
        sts.backward()
        time.sleep(8)
        sts.turnRight()
        time.sleep(1)
        sts.backward()
        time.sleep(2)
        sts.stop()
