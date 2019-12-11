import time
import sts

def initiate():
	sts.forward()
	time.sleep(1)
	sts.turnLeft()
	time.sleep(1.7)
	for i in range(4):
		sts.backward()
		time.sleep(1.5)
		sts.forward()
		time.sleep(1.5)
	sts.stop()
