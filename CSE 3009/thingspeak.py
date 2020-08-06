import time
import serial
import urllib2
ser = serial.Serial('COM7', 9600)
while True:
message = ser.readline()
print(message)
#print(message[19:21])
#print(message[41:43])
response =
urllib2.urlopen('https://api.thingspeak.com/update?api_key=WHZ8O385NPLNKEFJ&fie
ld1='+message[19:21]+'&field2='+message[41:43])
html = response.read()
time.sleep(0.5)
