import RPi.GPIO as GPIO
import time
import datetime, time
import os


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.IN)


alarmTime = datetime.time(hour = 11, minute = 13, second=0, microsecond=0)

##GPIO.output(18, True)
##time.sleep(1)
##GPIO.output(18, False)

while True:
    now = datetime.datetime.now().time()
    
    if GPIO.input(25)==True or now >= alarmTime: 
        GPIO.output(18, True)
        GPIO.output(23, True)
    else:
        GPIO.output(18, False)
        GPIO.output(23, False)
        
        

