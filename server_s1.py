#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Date: 24.12.2016

import socket           #Socketbefehle
import time             #für Zeitstempel bei den Nachrichten

host = "127.0.0.1"      #Der Server soll selbst der Host sein
port = 10000            #egal welcher, außer xy

clients = []            #Liste aller Clients

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))    #Socket wird an den Server gebunden
s.setblocking(0)        #Das Socket blockiert nicht-> immer wenn Daten ankommen,
                        #werden diese aus dem 'Stream' geladen

quitting = False
print("Server started...")

while quitting == False:
    try:
        data, addr = s.recvfrom(1024)
        if "Quit" in str(data):     #Quit in Nachricht --> Schleife Client Ende
            quitting = True
        if addr not in clients:     #Adresse nicht in Liste -> Hinzufügen
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + ": " + str(data))
        for client in clients:
            s.sendto(data, clients) #Nachricht an alle Clients
    except:
        pass
s.close()               #Wenn die Schleife endet, soll die Socket geschlossen werden
