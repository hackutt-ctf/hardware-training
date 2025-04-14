import serial
import serial.tools.list_ports
import time

def try_pin(ser, pin):
    ser.write(f"{pin}\n".encode())
    
    time.sleep(0.01)
    
    response = ""
    while ser.in_waiting > 0:
        response += ser.readline().decode().strip()
    return response

serial_port = serial.tools.list_ports.comports()
for port in serial_port:
    print(f"Port détecté : {port}")

ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
print(f"Connexion au port série : {ser}")
try_pin(ser, "help\n")
print(ser.readline().decode().strip())
for pin in range(10000):
    pin_str = f"unlock {pin:04d}"
    
    print(f"Tentative avec le code PIN : {pin_str}")
    response = try_pin(ser, pin_str)

    if "Code correct" in response:
        print(f"Code PIN trouvé : {pin_str}")
        break
    elif "Code incorrect" in response:
        print(f"Code PIN {pin_str} incorrect.")
    else:
        print(response)
        break

ser.close()

"""
$unlock aaaaaaaaaaaaaaaaaaaaaaaaaa
Error: Password too long! Maximum length is 16 characters.

"""
