import time
from datetime import datetime
from smtplib import SMTP
from smtplib import SMTPException
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import picamera
from time import sleep
from gpiozero import MotionSensor
from gpiozero import Button
from gpiozero import Buzzer


pir = MotionSensor(14)
bz = Buzzer(22)


while True:
    bz.off()
    print("Ready For Motion")
    if pir.wait_for_motion():
        start_time = time.time()
        print("Motion detected!")
        bz.on()
        bz.beep(0.5, 0.25, 8)
        sleep(1)
        bz.off()
        time.sleep(3)
        pir.wait_for_no_motion()
    
        with picamera.PiCamera() as camera:
           camera.resolution = (1024, 768)
           camera.start_preview()
           time.sleep(2)
           camera.capture('photo.jpg')

        
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
           
        except SMTPException as error:
              print "Error: unable to send email :  {err}".format(err=error)
        print("Email Sent")



