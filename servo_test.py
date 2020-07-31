from gpiozero import AngularServo
from time import sleep

# servo = Servo(9)

servo = AngularServo(9, min_angle=-90, max_angle=90)

angle = -90
direction = 1

while angle <= 90:
    servo.angle = angle
    sleep(0.1)
    angle += 5

#while True:
#    servo.min()
#    sleep(2)
#    servo.mid()
#    sleep(2)
#    servo.max()
#    sleep(2)

