from django.http import HttpResponse
from django.shortcuts import render
import sts
import car_patrols
import os


# Read config file
FILE_CONFIG = "/home/pi/app/config"

def forward(request):
	sts.forward()
	return HttpResponse("Forward")

def backward(request):
	sts.backward()
	return HttpResponse("Backward")

def stop(request):
	sts.stop()
	return HttpResponse("Stop")

#def motor_set_speed(request, speed):
#	speed = int(speed)
#	if speed < 24:
#		speed = 24
#	if speed > 100:
#		speed = 100
#	motor.setSpeed(speed)
#	text = "Speed set to", speed
#	return HttpResponse(text)

#def turning(request, angle):
#	angle = int(angle)
#	car_dir.turn(angle)
#	text = "Turing angle", angle
#	return HttpResponse(text)

def left(request):
	sts.turnLeft()
	return HttpResponse("Turning Left")

def right(request):
        sts.turnRight()
        return HttpResponse("Turning Right")

def scenario1(request):
	car_patrols.scenario1()
	return HttpResponse("Scenario1 Ran")

def scenario2(request):
	section = request.path[-1]
	if section == "A":
		car_patrols.sectionA()
		return HttpResponse("Section A Scanned")
	elif section == "B":
		car_patrols.sectionB()
		return HttpResponse("Section B Scanned")
	return HttpResponse("Unknown Section")
