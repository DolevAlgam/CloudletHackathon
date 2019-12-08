#!/usr/bin/env python
import time                  # Import necessary modules

MinPulse = 200
MaxPulse = 700

FILE_CONFIG = "/home/pi/Sunfounder_Smart_Video_Car_Kit_for_RaspberryPi/server/config"

Current_x = 0
Current_y = 0

def setup():
	pass
# Control the servo connected to channel 14 of the servo control board to make the camera 
# turning towards the positive direction of the x axis.
# ==========================================================================================
def move_decrease_x():
	pass
# ==========================================================================================
# Control the servo connected to channel 14 of the servo control board to make the camera 
# turning towards the negative direction of the x axis.
# ==========================================================================================
def move_increase_x():
	pass
# turning towards the positive direction of the y axis. 
# ==========================================================================================
def move_increase_y():
	pass
# ==========================================================================================
# Control the servo connected to channel 15 of the servo control board to make the camera 
# turning towards the negative direction of the y axis. 
# ==========================================================================================		
def move_decrease_y():
	pass
# move forward.
# ==========================================================================================
def home_x_y():
	pass

def calibrate(x,y):
	pass

def test():
	pass

if __name__ == '__main__':
	setup()
	home_x_y()
