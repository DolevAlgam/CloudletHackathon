#!/usr/bin/env python
import time    # Import necessary modules

# ===========================================================================
# Raspberry Pi pin11, 12, 13 and 15 to realize the clockwise/counterclockwise
# rotation and forward and backward movements
Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

# ===========================================================================
# Set channel 4 and 5 of the servo driver IC to generate PWM, thus 
# controlling the speed of the car
# ===========================================================================
EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5

# ===========================================================================
# Adjust the duty cycle of the square waves output from channel 4 and 5 of
# the servo driver IC, so as to control the speed of the car.
# ===========================================================================
def setSpeed(speed):
	pass

def setup():
	pass
# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will 
# move forward.
# ===========================================================================

def motor0(x):
	pass

def motor1(x):
	pass

def forward():
	pass

def backward():
	pass

def forwardWithSpeed(spd = 50):
	pass

def backwardWithSpeed(spd = 50):
	pass

def stop():
	pass

# ===========================================================================
# The first parameter(status) is to control the state of the car, to make it 
# stop or run. The parameter(direction) is to control the car's direction 
# (move forward or backward).
# ===========================================================================
def ctrl(status, direction=1):
	pass

def test():
	pass

if __name__ == '__main__':
	
	setup()
	setSpeed(50)
	#forward()
	#backward()
	stop()
	setup()
