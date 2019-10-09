import RPi.GPIO as GPIO, time

class StepperController:
    
    coil_A_1_pin = 0
    coil_A_2_pin = 0
    coil_B_1_pin = 0
    coil_B_2_pin = 0

    def __init__(self, pin1, pin2, pin3, pin4):
        self.coil_A_1_pin = pin1
        self.coil_A_2_pin = pin2
        self.coil_B_1_pin = pin3
        self.coil_B_2_pin = pin4
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)
        print ('pins set to output')
        print ('Pins Set')

    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.coil_A_1_pin, w1)
        GPIO.output(self.coil_A_2_pin, w2)
        GPIO.output(self.coil_B_1_pin, w3)
        GPIO.output(self.coil_B_2_pin, w4)

    def TurnMotor(self, direction, steps):
        StepPins = [
         self.coil_A_1_pin, self.coil_A_2_pin, self.coil_B_1_pin, self.coil_B_2_pin]
        Seq = [[1, 0, 0, 1],
         [
          1, 0, 0, 0],
         [
          1, 1, 0, 0],
         [
          0, 1, 0, 0],
         [
          0, 1, 1, 0],
         [
          0, 0, 1, 0],
         [
          0, 0, 1, 1],
         [
          0, 0, 0, 1]]
        StepCount = len(Seq)
        StepDir = direction
        WaitTime = 5 / float(1000)
        StepCounter = 0
        for i in range(0, steps):
            for pin in range(0, 4):
                xpin = StepPins[pin]
                if Seq[StepCounter][pin] != 0:
                    GPIO.output(xpin, True)
                else:
                    GPIO.output(xpin, False)

            StepCounter += StepDir
            if StepCounter >= StepCount:
                StepCounter = 0
            if StepCounter < 0:
                StepCounter = StepCount + StepDir
            time.sleep(WaitTime)

class ServoController:
    print ("hi")
