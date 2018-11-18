from gpiozero import MotionSensor
from gpiozero import Buzzer
from signal import pause
from time import sleep
from gpiozero import LED
from datetime import datetime
import time


red = LED(27)
pir = MotionSensor(17)


print("Waiting for PIR to settle")

while True:
    print("Ready for 1st One")
    pir.wait_for_motion()
    print("1st Sensor Motion detected!")
    red.on()
    sleep(5)
    pir.when_no_motion = red.off()



