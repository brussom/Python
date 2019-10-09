import RPi.GPIO as GPIO
import time
#import keyboard

GPIO.setmode(GPIO.BCM)     #Pin naming

redPin = 23
greenPin = 18
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.output(redPin, GPIO.LOW)
GPIO.output(greenPin,GPIO.LOW)


while True:
    msg = raw_input("Red Or Green?  ")
    if msg == "red":
        GPIO.output(redPin, GPIO.HIGH)
        GPIO.output(greenPin, GPIO.LOW)
        print ("Red On. Green Off")

    elif msg == "green":
        GPIO.output(redPin, GPIO.LOW)
        GPIO.output(greenPin, GPIO.HIGH)
        print ("Green On. Red Off.")
    elif msg == "christmas":
        GPIO.output(redPin, GPIO.HIGH)
        GPIO.output(greenPin, GPIO.HIGH)
        print ("Green On. Red Off.")
    
    else: 
        GPIO.output(redPin, GPIO.LOW)
        GPIO.output(greenPin, GPIO.LOW)
        print ("Both Off.")

  


    