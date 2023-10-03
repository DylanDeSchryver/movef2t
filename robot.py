import OPi.GPIO as GPIO
import time


class Tank:
    def __init__(self):
        # Configure GPIO pins for motor control
        self.motor1_forward_pin = 'PA8'  # Adjust GPIO pin numbers as needed
        self.motor1_backward_pin = 'PA9'
        self.motor2_forward_pin = 'PA10'
        self.motor2_backward_pin = 'PA20'

        GPIO.setmode(GPIO.SUNXI)
        GPIO.setup(self.motor1_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor1_backward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_forward_pin, GPIO.OUT)
        GPIO.setup(self.motor2_backward_pin, GPIO.OUT)

        self.motor1_fpwm = GPIO.PWM(self.motor1_forward_pin, 1000)  # 1000 Hz frequency
        self.motor2_fpwm = GPIO.PWM(self.motor2_forward_pin, 1000)
        self.motor1_bpwm = GPIO.PWM(self.motor1_backward_pin, 1000)  # 1000 Hz frequency
        self.motor2_bpwm = GPIO.PWM(self.motor2_backward_pin, 1000)

        self.motor1_fpwm.start(0)
        self.motor2_fpwm.start(0)
        self.motor1_bpwm.start(0)
        self.motor2_bpwm.start(0)

    def MOVEFWD(self):
        print('beofre')
        GPIO.output(self.motor1_forward_pin, GPIO.HIGH)
        print("after")
        GPIO.output(self.motor2_forward_pin, GPIO.HIGH)
        print("Hello WOrld")

    def MOVEBACKWARD(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_backward_pin, GPIO.HIGH)

    def TURNLEFT(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor1_backward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_backward_pin, GPIO.LOW)

    def TURNRIGHT(self):
        GPIO.output(self.motor1_forward_pin, GPIO.HIGH)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.LOW)
        GPIO.output(self.motor2_backward_pin, GPIO.HIGH)

    def STOP(self):
        GPIO.output(self.motor1_forward_pin, GPIO.LOW)
        GPIO.output(self.motor2_forward_pin, GPIO.LOW)
        GPIO.output(self.motor1_backward_pin, GPIO.LOW)
        GPIO.output(self.motor2_backward_pin, GPIO.LOW)
        self.motor1_fpwm.ChangeDutyCycle(0)  # Stop PWM
        self.motor2_fpwm.ChangeDutyCycle(0)
        self.motor1_bpwm.ChangeDutyCycle(0)  # Stop PWM
        self.motor2_bpwm.ChangeDutyCycle(0)

    def SETSPEED(self, speed):
        self.motor1_fpwm.ChangeDutyCycle(speed)
        self.motor2_fpwm.ChangeDutyCycle(speed)
        print("Hello Daniel")

    def cleanup(self):
        GPIO.cleanup()
        self.motor1_fpwm.stop()
        self.motor2_fpwm.stop()
        self.motor1_bpwm.stop()
        self.motor2_bpwm.stop()
