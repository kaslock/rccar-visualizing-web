import sys

sys.path.append('./Raspi-MotorHAT-python3')

from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
from Raspi_PWM_Servo_Driver import PWM
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from pymysql import *
import atexit
import time

import Adafruit_DHT as dht
from gpiozero import DistanceSensor
# from picamera import PiCamera
# from PIL import Image

class pollingThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        
        try:
            self.db = connect(
                host="54.180.32.208",
                user="dev8_1",
                password="1234",
                db="dev8",
                )
            print("OK!")
        except:
            print("ERROR!")
            exit(1)
        self.cur = self.db.cursor()

        self.mh = Raspi_MotorHAT(addr=0x6f)
        self.myMotor = self.mh.getMotor(1)
        self.myMotor.setSpeed(50)

        self.pwm = PWM(0x6F)
        self.pwm.setPWMFreq(60)
        self.dist_sensor = DistanceSensor(20, 21) # Echo Trig
        self.cnt = 30

        # self.camera = PiCamera()
        # self.camera.start_preview()

        while True:
            qdt = QDateTime().currentDateTime()
            self.dt = qdt.toString("yyyy-MM-dd HH:mm:ss")

            if self.cnt == 30:
                self.h,self.t = dht.read_retry(dht.DHT11,14)
                self.cnt = 0

            self.getQuery()
            
            if self.cnt % 10 == 0:
                # self.camera.capture('/home/pi/Pictures/image.jpg')
                self.setQuery()
                
            time.sleep(0.1)
            self.cnt += 1

    def getQuery(self):
        self.cmd = "select * from command1 order by time desc limit 1";
        self.cur.execute(self.cmd)
        self.db.commit()
        self.data = self.cur.fetchall()

        cmdTime = self.data[0][0]
        cmdType = self.data[0][1]
        cmdArg = self.data[0][2]
        is_finish = self.data[0][3]

        if is_finish == 0 :
            #detect new command
            print(cmdTime, cmdType, cmdArg)

            #update
            self.cmd = "update command1 set is_finish=1 where is_finish=0";
            self.cur.execute(self.cmd)
            self.db.commit()

            #motor
            if cmdType == "go": self.go()
            if cmdType == "back": self.back()
            if cmdType == "left": self.left()
            if cmdType == "right": self.right()
            if cmdType == "mid": self.middle()

        is_finish = 1

    def setQuery(self):
        self.sens = "insert into `sensing1` (`time`, `num1`, `num2`, `num3`, \
        `meta_string`, `is_finish`) VALUES ('{0}', '{1}', '{2}', '{3}', '0', '0')".format(self.dt, self.h, self.t, self.dist_sensor.distance)
        self.cur.execute(self.sens)
        self.db.commit()


    def go(self):
        print("MOTOR GO")
        self.myMotor.setSpeed(50)
        self.myMotor.run(Raspi_MotorHAT.FORWARD)
        #time.sleep(1)
        #self.myMotor.run(Raspi_MotorHAT.RELEASE)

    def back(self):
        print("MOTOR BACK")
        #self.myMotor.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor.run(Raspi_MotorHAT.RELEASE)
    
    def left(self):
        print("MOTOR LEFT")
        self.pwm.setPWM(0, 0, 250);
    
    def right(self):
        print("MOTOR RIGHT")
        self.pwm.setPWM(0, 0, 440);
    
    def middle(self ):
        print("MOTOR MIDDLE")
        self.pwm.setPWM(0, 0, 345);

th = pollingThread()
th.start()
# app = QApplication()

#infinity loop
while True:
    pass