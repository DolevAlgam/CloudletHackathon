import novideo_dir as video_dir
import nocar_dir as car_dir
import nomotor as motor
import time

def scenario1():
	motor.forward()
	time.sleep(5)
	motor.ctrl(0)

def sectionA():
	motor.forward()
	time.sleep(3)
	car_dir.turn_right()
	time.sleep(2)
	motor.ctrl(0)

def sectionB():
	motor.forward()
        time.sleep(2)
        car_dir.turn_left()
        time.sleep(3)
        motor.ctrl(0)

