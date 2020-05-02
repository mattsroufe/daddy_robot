import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# red
GPIO.setup(22,GPIO.OUT)
print("LED on")
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(22,GPIO.LOW)

# green
GPIO.setup(27,GPIO.OUT)
print("LED on")
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(27,GPIO.LOW)

# blue
GPIO.setup(24,GPIO.OUT)
print("LED on")
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(24,GPIO.LOW)

