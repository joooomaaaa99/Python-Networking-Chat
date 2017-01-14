#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date: 24.12.2016

import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while shutdown == False:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release()

host = "127.0.0.1"
port = 0                        #freier Port wird genutzt

server = ("127.0.0.1", 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

rT = threading.Threa(target=receving, args = ("RecvThread"), s)
rT.start()

alias = raw_input("Dein Name: ")
message = raw_input("Deine Nachricht: ")

while message != "q":           #Befehl zum beenden des Chats
    if message != "":           #Leere Nachrichten werden nicht gesendet
        s.sendto(alias + ":" + message, server)
        tLock.acquire()
        message = raw_input(alias + ": ")
        time.sleep(0.2)
shutdown = True
rT.join()
s.close()
