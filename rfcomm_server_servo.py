#!/usr/bin/python

import bluetooth
import os
import os.path
import time

pwm_period = 0.0

def pwm_open():
    os.system('sudo echo 0 > /sys/class/pwm/pwmchip0/export')
    os.system('sudo echo "normal" > /sys/class/pwm/pwmchip0/pwm0/polarity')

def pwm_enable():
    os.system('sudo echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable')

def pwm_stop():
    os.system('sudo echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable')

def pwm_close():
    os.system('sudo echo 0 > /sys/class/pwm/pwmchip0/unexport')
 
def pwm_freq(freq):
    global pwm_period
    pwm_period = 1000000000.0 / freq
    os.system('sudo echo ' + str(int(pwm_period)) + ' > /sys/class/pwm/pwmchip0/pwm0/period')

def pwm_duty(duty):
    dutycycle = duty * int(pwm_period)
    os.system('sudo echo ' + str(int(dutycycle)) + ' > /sys/class/pwm/pwmchip0/pwm0/duty_cycle')

pwm_open()
pwm_freq(50)
pwm_duty(0.05)              # min 0.05, max 0.15 180 degrees
pwm_enable()

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
		
		if data == "stop":
			pwm_stop()
			send_data = "Stop "
		elif data == "middle":
			pwm_duty(0.1)
			send_data = "Middle "
		elif data == "right":
			pwm_duty(0.05)
			send_data = "Right "
		elif data == "left":
			pwm_duty(0.15)
			send_data = "Left "
		else:
			send_data = "Error "
		# Sending the data.
		client.send(send_data) 
except:
        pwm_close()
	# Closing the client and server connection
	client.close()
	server.close()
