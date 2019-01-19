import RPi.GPIO as GPIO
import time
import datetime, time
import os

button=25
led1=18
led2=23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

#PWM controls dimming
pwm1=GPIO.PWM(led1, 1000)
pwm2=GPIO.PWM(led2, 1000)

pwm1.start(0)
pwm2.start(0)
brightness=1

#Set the wakeup alarm time
alarmTime = datetime.time(hour = 14, minute = 59, second=30, microsecond=0)

isTime=0

#Check the current time
while True:
        now=datetime.datetime.now().time()
        if now >=alarmTime:
                isTime=1
                break

#If its the specified alarm time dim and brighten the LEDs
dimming =0
while (isTime==1): 
        while (dimming == 0):
                brightness=brightness*1.2
                if brightness >100:
                        brightness=100
                        dimming=1
                pwm1.ChangeDutyCycle(brightness)
                pwm2.ChangeDutyCycle(brightness)
                time.sleep(.05)
        if GPIO.input(button):
                isTime=0
                break;
        while (dimming == 1):
                brightness=brightness/1.2
                if brightness<1:
                        brightness=1
                        dimming = 0
                pwm1.ChangeDutyCycle(brightness)
                pwm2.ChangeDutyCycle(brightness)
                time.sleep(.05)
        if GPIO.input(button):
                isTime=0
                break;
                
GPIO.output(led1, False)
GPIO.output(led2, False)
                
                #GPIO.output(led1, True)
                #GPIO.output(led2, True)
        
#Turn off the LEDs if the button is pressed
#while True:
 #       if GPIO.input(button):
  #              GPIO.output(led1, False)
   #             GPIO.output(led2, False)
    #            break;
        
        

