from gpiozero import MotionSensor
from gpiozero import Buzzer
from signal import pause
from time import sleep
from gpiozero import LED
from datetime import datetime
import time
from gpiozero import Button
from smtplib import SMTP
from smtplib import SMTPException
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import picamera




pir = MotionSensor(14)
button = Button(2)

def Capture_Photo():
    with picamera.PiCamera() as camera:
           camera.resolution = (1024, 768)
           camera.start_preview()
           time.sleep(2)
           camera.capture('photo.jpg')
    

def Sent_Mail():
    f_time = datetime.now().strftime('%a %d %b @ %H:%M')
        
    print("Sending Email...")
    toaddr = 'surana129@gmail.com'    
    me = 'team8640@gmail.com' 
    subject = 'Photo ' + f_time

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "Photo @ " + f_time

    fp = open('photo.jpg', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)

    try:
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user = 'team8640@gmail.com',password = 'ranarimasima')
        s.sendmail(me, toaddr, msg.as_string())
        s.quit()
        print("Email Sent")
           
    except SMTPException as error:
        print "Error: unable to send email :  {err}".format(err=error)
        




print("Waiting for PIR to settle")

while True:
    print("Ready for Motion")
    motion = pir.wait_for_motion()
    motion_time = time.time()
    if motion == True:
        print("Motion Detected")
        print("Capturing Photo...")
        Capture_Photo()
        print("Waiting for button press...")
        
        status = button.wait_for_press(10)
        button_time = time.time()
        print(button_time - motion_time)
        if status == True:
            print("Button Pressed and detected as guest")
            Sent_Mail()
            sleep(button_time - motion_time)
        else:
            print("Button is not pressed. go for auto")
            Sent_Mail()
            




