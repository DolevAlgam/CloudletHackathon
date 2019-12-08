import explorerhat
# left =  two , right = one

def circle():
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.backwards()

def stop():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def forward():
    explorerhat.motor.one.forwards()
    explorerhat.motor.two.forwards()

def backward():
    explorerhat.motor.one.backwards()
    explorerhat.motor.two.backwards()

def setSpeed(speed, side):
    if side == "left":
	explorerhat.motor.two.speed(speed)
    elif side == "right":
	explorerhat.motor.one.speed(speed)
    explorerhat.motor.speed(speed)

def turnLeft(current_speed):
	explorerhat.motor.two.stop()
	explorerhat.motor.one.forwards(100)

def turnRight():
	explorerhat.motor.one.stop()
        explorerhat.motor.two.forwards(100)

#def map(n, start1, stop1, start2, stop2):
#	return ((n-start1)/(stop1-start1))*(stop2-start2)+start2
