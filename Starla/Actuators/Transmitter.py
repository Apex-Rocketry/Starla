import time
import serial

import sys
sys.path.append("/home/pi/Components")
from MPU6050.MPU6050_Readings import MPU6050
from BME280.BME280_Readings import BME280

BME280 = BME280()
MPU6050 = MPU6050()
t = time.time()

class Transmitter:
    def __init__(self):
        self.ser = serial.Serial(
                       port="/dev/ttyAMA0",
                       baudrate=9600,
                       parity=serial.PARITY_NONE,
                       stopbits=serial.STOPBITS_ONE,
                       bytesize=serial.EIGHTBITS,
                       timeout=1
                   )

    def sendSensorsData(self, delay):
        while 1:
            msg = "$"
            msg += str(round(time.time()-t, 2)) + ","
            c = ""
            for i in range(len(MPU6050.dataPackage())):
                msg += c + str(MPU6050.dataPackage()[i])
                c = ","
            for i in range(len(BME280.dataPackage())):
                msg += c + str(BME280.dataPackage()[i])
                c = ","
            msg += "#"
            self.ser.write(msg)
            print(msg + "\n")
            msg = ""
            time.sleep(delay)

    def sendRescueData(self, delay):
        pass