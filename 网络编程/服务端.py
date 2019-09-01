#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8000))
server.listen(5)


while True:
    conn,client = server.accept()
    print(client)
    while True:
        try:
            msg = conn.recv(1024)
            print(msg.decode('utf8'))
            conn.send('hello'.encode('utf8'))
        except Exception as e:
            conn.close()

server.close()


