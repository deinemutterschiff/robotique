from unifr_api_epuck import wrapper

MY_IP = '192.168.2.211'
robot = wrapper.get_robot
counter = 0

while robot.go_on() and counter < 400:
    counter += 1
    if counter % 80 < 40:
        robot.set_speed(2, 2)
    else :
        robot.set_speed(-2, -2)

robot.clean_up()
