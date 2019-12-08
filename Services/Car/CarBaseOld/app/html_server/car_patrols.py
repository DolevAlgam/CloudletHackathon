import novideo_dir as video_dir
import nocar_dir as car_dir
import nomotor as motor
import time
import requests

def scanSuspect():
	r = requests.get('http://jetson/scan')
        if r.text == "attack":
                motor.setSpeed(200)
                motor.forward()
                time.sleep(1)
                motor.ctrl(0)
	return r.text

def scenario1():
	motor.forward()
	time.sleep(5)
	motor.ctrl(0)
	scanSuspect()
	if r.text != "attack":
		motor.backward()
		time.sleep(5)
		motor.ctrl(0)

def sectionA():
	motor.forward()
	time.sleep(3)
	car_dir.turn_right()
	time.sleep(2)
	motor.ctrl(0)
	scanSuspect()
        if r.text != "attack":
                motor.backward()
                time.sleep(2)
		car_dir.turn_right()
	        time.sleep(3)
                motor.ctrl(0)

def sectionB():
	motor.forward()
        time.sleep(2)
        car_dir.turn_left()
        time.sleep(3)
        motor.ctrl(0)
	scanSuspect()
        if r.text != "attack":
                motor.backward()
                time.sleep(3)
                car_dir.turn_right()
                time.sleep(2)
                motor.ctrl(0)

