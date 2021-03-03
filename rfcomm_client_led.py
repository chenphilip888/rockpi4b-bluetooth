#!/usr/bin/python3

import bluetooth
import time

bd_addr = "6C:21:A2:41:BD:03"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

for i in range( 5 ):
    sock.send("1")
    print(sock.recv(1024))
    time.sleep( 1 )
    sock.send("0")
    print(sock.recv(1024))
    time.sleep( 1 )

sock.close()
