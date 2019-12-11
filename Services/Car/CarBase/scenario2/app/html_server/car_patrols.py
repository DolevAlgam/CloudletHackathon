import time
import sts

def initiate():
	sts.forward()
	time.sleep(1)
	sts.turnLeft()
	time.sleep(2)
	for i in range(10):
		sts.backward()
		time.sleep(3)
		sts.forward()
		time.sleep(3)
