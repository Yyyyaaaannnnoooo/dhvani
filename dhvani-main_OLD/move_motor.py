import serial


import time

try:
    arduino = serial.Serial('/dev/ttyACM0')
except:
    arduino = serial.Serial('/dev/ttyACM1')

time.sleep(2)
command = '100'
arduino.write(command.encode())