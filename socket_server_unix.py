#!/usr/bin/python

import socket
import os
import sys
import signal

SOCKET_FD = "/tmp/python_unix_sockets_example"
server = None

def signal_handler(signal, frame):
    print("Received keyboard interrupt; shutting down.")
    if server:
        server.close()
    if os.path.exists(SOCKET_FD):
        os.remove(SOCKET_FD)
    print("Exiting.")
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

if os.path.exists(SOCKET_FD):
    os.remove(SOCKET_FD)

print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FD)

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    print("-" * 20)
    msg = datagram.decode('utf-8')
    print(msg)
    if "DONE" == msg:
        print "Done!"
        break
print("-" * 20)
print("Shutting down...")
server.close()
os.remove(SOCKET_FD)
print("Exiting.")
