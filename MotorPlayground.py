
import MotorControl
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
print ("Imported ServoKit")
print ("Change to test GitHub")

currentPos = 0
DesiredPosition =0

#sorter = MotorControl.StepperController(20,22,24,4)
#sorter.setStep(0,0,0,0)
servo = MotorControl.ServoController(26)
print ("pins freed")
numSteps = 512
speed = 2
Direction = speed *-1

try:
  while True:
      #sorter.TurnMotor(speed, numSteps)
        #print ("moved back")
        for i in range(0,36):
          x = i*5
          print (x)
          servo.cycleMotor(x)
          #servo.cycleMotor(90)
          #servo.cycleMotor(180)
except KeyboardInterrupt:
  
 # GPIO.output(20, False)
 # GPIO.output(22, False)
 # GPIO.output(24, False)
 # GPIO.output(4, False)
  GPIO.output(26, False)

   