import serial
import time

s = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

time.sleep(1)

while(1):
    s.flush()
    s.write(b'10010000000')
    res = s.readline()
    print(res)
    if (res.strip().decode() == 'configed'):
        break


arr_float = [0.1, 0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
for i in arr_float:
    s.flush()
    print(str(i).encode() + b'\n')
    s.write(str(i).encode() + b'\n')
    
for i in range(8):
    print(s.readline())