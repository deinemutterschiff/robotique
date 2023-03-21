# run the code to generate IR sensor data 
from unifr_api_epuck import wrapper
import signal
import time
import sys

LEFT = 2
MID = 1
RIGHT = 0

STEPS = 300

state = "forward"

MY_IP = '192.168.2.208'

robot = wrapper.get_robot(MY_IP)

robot.init_ground()

def signal_handler(sig, frame):
	robot.clean_up()

signal.signal(signal.SIGINT, signal_handler)

while robot.go_on() :
    gs = robot.get_ground()
    
    if (gs[LEFT] < 500 and gs[MID] < 500 and gs[RIGHT] < 500) :
    	if (state == "turn_l") :
    		robot.set_speed(0, 2)
    		time.sleep(3)
    	if (state == "turn_r") :
    		robot.set_speed(2, 0) 
    		time.sleep(3)
    
    if (gs[LEFT] > 500 and (gs[RIGHT] < 500 or gs[MID] < 500)) :
    	robot.set_speed(1, 2)
    	state = "turn_l"
    elif (gs[RIGHT] > 500 and (gs[LEFT] < 500 or gs[MID] < 500)) :
    	robot.set_speed(2, 1)
    	state = "turn_r"
    else :
    	robot.set_speed(2, 2)
