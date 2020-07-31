from time import sleep
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from camera import VideoCamera
from gpiozero import AngularServo
# import RPi.GPIO as GPIO

#servos
# ServoPinJ1 = AngularServo(23, min_angle=-90, max_angle=90)
# ServoPinJ2 = AngularServo(11, min_angle=-90, max_angle=90)
# ServoPinJ3 = AngularServo(9, min_angle=-90, max_angle=90)
# ServoPinJ1 = 23
# ServoPinJ2 = 11
# ServoPinJ3 = 9

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('move-servo')
def handle_move_servo_event(json, methods=['GET', 'POST']):
    # global servo_j2_position
    # global pwm_servo_j2
    # servo_j2_position = servo_j2_position + json.get('x')
    # print(servo_j2_position)
    # setServoAngle(pwm_servo_j2, servo_j2_position)
    # setServoAngle(pwm_servo_j3, servo_j3_position = servo_j3_position + json.get('y'))
    print('received move servo event: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    # ServoPinJ1.angle = 30
    # ServoPinJ2.angle = 60
    # ServoPinJ3.angle = 90
    app.run(host='0.0.0.0', debug=True)

