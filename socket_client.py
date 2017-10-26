#!/usr/bin/python

import socket
import os
import sys

SOCKET_FD = "/tmp/python_unix_sockets_example"

print("Client connecting...")
if not os.path.exists(SOCKET_FD):
    print("Couldn't connect!")
    print("Exiting.")
    sys.exit()

client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
client.connect(SOCKET_FD)
print("Ready; press Ctrl-C to quit.")
print("Sending 'DONE' shuts down both client and server gracefully.")
while True:
    try:
        x = raw_input("> ")
        if "" == x:
            continue
        print("SEND:", x)
        msg = x.encode('utf-8')
        client.send(msg)
        if "DONE" == x:
            print("'DONE' received. Shutting down.")
            break
    except KeyboardInterrupt as k:
        print("Received keyboard interrupt; shutting down.")
        break

client.close()
print("Exiting.")
