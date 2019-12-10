import os
import time
import serial
import pandas as pd

portaSerial = serial.Serial(
   
    port='COM6',
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
while(time.time() - delayTrash <= 10):
    trash = portaSerial.readline(4)

delayData = time.time()
while ((time.time() - delayData <= 30)):
    sensorData += str(portaSerial.readline(4))[2:-1]
#exclude first and last data signal
sensorData = sensorData[sensorData.find("\\")+2:sensorData.rfind("n")-1]

for i in range(len(sensorData)):
    logFile.write(sensorData[i])
logFile.close()

with open("logSensor.txt", "rt") as log:
    with open("out.txt", "wt") as out:
        for line in log:
            out.write(line.replace("\\n", '\n'))
out.close()
log.close()

signalData = list(map(int,sensorData.split("\\n")))
dict = {'hart': signalData}
df = pd.DataFrame(dict)
df.to_csv('out.csv', index=False)

exit()