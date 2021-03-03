#!/usr/bin/python3

import bluetooth
import time

bd_addr = "6C:21:A2:41:BD:03"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

for i in range( 5 ):
    sock.send("red")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("green")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("blue")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("yellow")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("cyan")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("purple")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("white")
    print(sock.recv(1024))
    time.sleep( 0.8 )
    sock.send("black")
    print(sock.recv(1024))
    time.sleep( 0.8 )

sock.send( "Hello world !\nIt works !\n" )
print(sock.recv(1024))
sock.close()
