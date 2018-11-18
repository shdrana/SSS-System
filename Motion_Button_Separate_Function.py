from gpiozero import MotionSensor
from gpiozero import Buzzer
from signal import pause
from time import sleep
from gpiozero import LED
from datetime import datetime
import time
from gpiozero import Button


red = LED(27)
pir = MotionSensor(17)
button = Button(22)



def SendGuestEnranceMessaage(message):
    print(message)

def SendSuspiciousMessage(message):
    print(message)



print("Waiting for PIR to settle")

while True:
    print("Ready for Motion")
    motion = pir.wait_for_motion()
    motion_time = time.time()
    if motion == True:
        print("Motion Detected")
        red.on()
        print("Wait for button Press")
        status = button.wait_for_press(10)
        button_time = time.time()
        print(button_time - motion_time)
        if status == True:
            SendGuestEnranceMessaage("Button Pressed and detected as guest")
            sleep(button_time - motion_time)
        else:
            SendSuspiciousMessage("Button is not pressed. go for auto")
            
        
    pir.when_no_motion = red.off()







