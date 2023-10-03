import robot
import time
import OPi.GPIO as GPIO

from robot import Tank

tank = robot.Tank()

tank.STOP()
tank.MOVEFWD()
tank.SETSPEED(50)
time.sleep(5)
tank.STOP()
GPIO.cleanup()
