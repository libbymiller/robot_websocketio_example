import socketio
# you need the right version
# see https://github.com/miguelgrinberg/python-socketio/issues/586#issuecomment-754069602

# servo stuff
from gpiozero import Servo
from gpiozero import AngularServo
from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

from time import sleep

last_lr = 0
last_ud = 0

def pan(to):
   global last_lr
   print("panning to",to)
   servo_lr.angle = to
   last_lr = to

def tilt(to):
   global last_ud
   servo_ud.angle = to
   last_ud = to
# end servo stuff

sio = socketio.Client()
# for logging
# sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
    print('connection established')

@sio.event
def message(data):
        command = data
        print("command",command)

        # I've just put a few of the commands in
        if(command == "left_a_bit"):
           p = last_lr
           try:
             pan(p+10)
             sio.emit('message', {"ok":command})
           except:
             sio.emit('message', {"nok":command})
             traceback.print_exc()

        if(command == "right_a_bit"):
          p = last_lr
          try:
            pan(p-10)
            sio.emit('message', {"ok":command})
          except:
            sio.emit('message', {"nok":command})
            traceback.print_exc()

        if(command == "down_a_bit"):
          t = last_ud
          try:
            print("t - down a bit",t)
            tilt(t+10)
            sio.emit('message', {"ok":command})
          except:
            sio.emit('message', {"nok":command})
            traceback.print_exc()

        if(command == "up_a_bit"):
          t = last_ud
          try:
            if(t-10 >=30):
              tilt(t-10)
              sio.emit('message', {"ok":command})
            else:
              sio.emit('message', {"nok":command})
              print("too far back!")
          except:
            sio.emit('message', {"nok":command})
            traceback.print_exc()

        if(command == "gone"):
            pass
        if(command == "arrived"):
            pass
        if(command == "hello"):
            pass
        if(command == "leaving"):
            pass
        if(command == "left"):
            pass
        if(command == "right"):
            pass
        if(command == "halt"):
            pass

# this catch-all appears not to work
# but logging does

@sio.on('*')
def catch_all(event, data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')


# initialise the servos
servo_ud = AngularServo(17, min_angle=0, max_angle=180)
servo_lr = AngularServo(23, min_angle=0, max_angle=180)

pan(90)
tilt(90)

# socket.io is assumed to be at https://myserver/socket.io/socket.io.js
sio.connect('https://myserver/')
