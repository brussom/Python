<<<<<<< HEAD
import MotorControl
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
print ("Imported ServoKit")
currentPos = 0
DesiredPosition =0

sorter = MotorControl.StepperController(20,22,24,4)
sorter.setStep(0,0,0,0)
print ("pins freed")
numSteps = 512
speed = 2
Direction = speed *-1

try:
  while True:
      sorter.TurnMotor(speed, numSteps)
        #print ("moved back")
except KeyboardInterrupt:
  
  GPIO.output(20, False)
  GPIO.output(22, False)
  GPIO.output(24, False)
  GPIO.output(4, False)
=======
import MotorControl
import RPi.GPIO as GPIO

currentPos = 0
DesiredPosition =0

sorter = MotorControl.StepperController(20,22,24,4)
sorter.setStep(0,0,0,0)
print ("pins freed")
numSteps = 512
speed = 2
Direction = speed *-1

try:
  while True:
      sorter.TurnMotor(speed, numSteps)
        #print ("moved back")
except KeyboardInterrupt:
  
  GPIO.output(20, False)
  GPIO.output(22, False)
  GPIO.output(24, False)
  GPIO.output(4, False)
>>>>>>> 16e93d9beb5cb02bc019b91a7d5777294b6ab9e8
   