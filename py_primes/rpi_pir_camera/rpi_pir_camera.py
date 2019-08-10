import time
from datetime import datetime

import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
camera = PiCamera()
camera.resolution = (1024, 768)
# Camera warm-up time
time.sleep(2)

i = GPIO.input(11)

while True:
    if GPIO.input(11) != 0:
        camera.capture('img' + datetime.now().strftime('%Y-%m-%d---%H:%M:%S') + '.jpg')
        time.sleep(2)
