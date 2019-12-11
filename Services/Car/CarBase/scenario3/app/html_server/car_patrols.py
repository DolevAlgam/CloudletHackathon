import time
import sts

def scanSuspect():
	time.sleep(2)
        if True:
                sts.setSpeed(100)
                sts.forward()
                time.sleep(2)
                sts.stop()
		time.sleep(1)

def initiate():
	sts.forward()
	time.sleep(5)
	sts.stop()
	scanSuspect()
	sts.backward()
	time.sleep(5)
	sts.stop()
