import serial # type: ignore
import time

ser = serial.Serial(
   port=1,
   baudrate=9600,
   parity=serial.PARITY_ODD,
   stopbits=serial.STOPBITS_TWO,
   bytesize=serial.SEVENBITS
)

input = 1
while 1:
    # get keyboard input
    input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        ser.write(input + '\r\n')
        out = ''

time.sleep(1)
while ser.inWaiting() > 0:
   out += ser.read(1)

if out != '':
   print
   ">>" + out

