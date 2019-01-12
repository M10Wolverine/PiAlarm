import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    if GPIO.input(25):
        GPIO.output(18, True)
        GPIO.output(23, True)
    else:
        GPIO.output(18, False)
        GPIO.output(23, False)
        
