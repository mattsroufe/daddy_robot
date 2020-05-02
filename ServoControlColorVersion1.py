#-*- coding:UTF-8 -*-
#This code uses the PWM library that comes with the system.
import RPi.GPIO as GPIO
import time

#Definition of servo pin
ServoPinJ1 = 23
ServoPinJ2 = 11
ServoPinJ3 = 9

ServoPin = ServoPinJ2

#Set the GPIO port to BCM encoding mode.
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#RGB module pins are initialized into output mode
#Servo pin is initialized into input mode
def init():
    global pwm_servo
    GPIO.setup(ServoPin, GPIO.OUT)
    pwm_servo = GPIO.PWM(ServoPin, 50)
    pwm_servo.start(0)
		
def servo_control_color():
    for pos in range(181):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
	time.sleep(0.009) 
    for pos in reversed(range(181)):
        pwm_servo.ChangeDutyCycle(2.5 + 10 * pos/180)
	time.sleep(0.009)

#The try/except statement is used to detect errors in the try block.
#the except statement catches the exception information and processes it.
try:
    init()
    pwm_servo.ChangeDutyCycle(2.5 + 10 * 90/180)
    while True:
 	servo_control_color()
		
except KeyboardInterrupt:
    pass
pwm_servo.stop()
GPIO.cleanup()
