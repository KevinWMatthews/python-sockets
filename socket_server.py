#!/usr/bin/python

import socket
import os

SOCKET_FD = "/tmp/python_unix_sockets_example"
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
