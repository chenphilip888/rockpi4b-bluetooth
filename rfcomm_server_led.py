#!/usr/bin/python

import bluetooth
import os
import os.path
import time
import sys

led = 154

def check_already_exported(pinnum):
    path = '/sys/class/gpio/gpio' + str(pinnum)
    isdir = os.path.isdir(path)
    return isdir

def initpin(pinnum, mode):
    '''
    pinnum: pin number, eg. 172, 175 etc.
    mode: pin mode, valid values: in or out
    '''
    if not check_already_exported(pinnum):
        with open('/sys/class/gpio/export', 'w') as f:
            f.write(str(pinnum))
        with open('/sys/class/gpio/gpio' + str(pinnum) + '/direction', 'w') as f:
            f.write(str(mode))

def setpin(pinnum, value):
    with open('/sys/class/gpio/gpio' + str(pinnum) + '/value', 'w') as f:
        f.write(str(value))

def getpin(pinnum):
    with open('/sys/class/gpio/gpio' + str(pinnum) + '/value', 'r') as f:
        value = f.read() 
        return int(value)

def closepin(pinnum):
    with open('/sys/class/gpio/unexport', 'w') as f:
        f.write(str(pinnum))

initpin(led, 'out')

host = ""
port = 1	# Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
	server.bind((host, port))
	print("Bluetooth Binding Completed")
except:
	print("Bluetooth Binding Failed")
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address. 
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
try:
	while True:
		# Receivng the data. 
		data = client.recv(1024) # 1024 is the buffer size.
		# print(data)
		
		if data == "1":
			setpin(led, 1)
			send_data = "Light On "
		elif data == "0":
			setpin(led, 0)
			send_data = "Light Off "
		else:
			send_data = "Type 1 or 0 "
		# Sending the data.
		client.send(send_data) 
except:
        closepin(led)
	# Closing the client and server connection
	client.close()
	server.close()
