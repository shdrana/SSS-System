import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) #PIR
GPIO.setup(27, GPIO.OUT) #BUzzer
pir = 17
led = 27

time.sleep(2) # to stabilize sensor

while True:
    if GPIO.input(pir):
        GPIO.output(led, True)
        time.sleep(0.5) #led turns on for 0.5 sec
        GPIO.output(led, False)
        print("Motion Detected...")
        time.sleep(5) #to avoid multiple detection

    time.sleep(0.1) #loop delay, should be less than detection delay


