import RPi.GPIO as GPIO
import time
import datetime, time
import os


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.IN)


alarmTime = datetime.time(hour = 11, minute = 29, second=0, microsecond=0)

isTime=0

while True:
        now=datetime.datetime.now().time()
        if now >=alarmTime:
                isTime=1
                break

if isTime==1:
    if now >= alarmTime: 
        GPIO.output(18, True)
        GPIO.output(23, True)
        
while True:
        if GPIO.input(25):
                GPIO.output(18, False)
                GPIO.output(23, False)
                break;
        
        

