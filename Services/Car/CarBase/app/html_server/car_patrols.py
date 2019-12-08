import time
import requests
import sts

def scanSuspect():
	r = requests.get('http://jetson/scan')
        if r.text == "attack":
                sts.setSpeed(100)
                sts.forward()
                time.sleep(1)
                sts.stop()
	return r.text

def scenario1():
	sts.forward()
	time.sleep(5)
	sts.stop()
	scanSuspect()
	if r.text != "attack":
		sts.backward()
		time.sleep(5)
		sts.stop()

def sectionA():
	sts.forward()
	time.sleep(3)
	sts.turnRight()
	time.sleep(2)
	sts.stop()
	scanSuspect()
        if r.text != "attack":
                sts.backward()
                time.sleep(2)
		sts.turnRight()
	        time.sleep(3)
                sts.stop()

def sectionB():
	sts.forward()
        time.sleep(2)
        sts.turnLeft()
        time.sleep(3)
        sts.stop()
	scanSuspect()
        if r.text != "attack":
                sts.backward()
                time.sleep(3)
                sts.turnRight()
                time.sleep(2)
                sts.stop()
