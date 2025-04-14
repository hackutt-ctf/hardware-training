import serial

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.write(b'AT+MEMDUMP=0x0000000,256\r\n')
while True:
    line = ser.readline().decode().strip()
    if not line:
        break
    print(line)

ser.close()
