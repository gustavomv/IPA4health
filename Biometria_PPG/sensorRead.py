import time
import serial
import os


portaSerial = serial.Serial(
   
    port='COM7',
    baudrate = 115200,
    #parity=serial.PARITY_NONE,
    #stopbits=serial.STOPBITS_ONE,
    #bytesize=serial.EIGHTBITS,
    timeout=1
)
counter = 0
sensorData = ""

logFile = open("logSensor.txt", "w+")

delayTrash = time.time()
while(time.time() - delayTrash <= 5):
    trash = portaSerial.readline(4)

delayData = time.time()
while ((time.time() - delayData <= 3*60)):
    sensorData += str(portaSerial.readline(4))[2:-1]
        
for i in range(len(sensorData)):
    logFile.write(sensorData[i])
logFile.close()

with open("logSensor.txt", "rt") as log:
    with open("out.txt", "wt") as out:
        for line in log:
            out.write(line.replace("\\n", '\n'))
exit()
