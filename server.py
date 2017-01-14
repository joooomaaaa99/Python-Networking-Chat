"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 11.01.2017
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)					#Socket des Moduls Socket wird erstellt
s.bind(("", 50000))														#.bind benötigt Tupel als Eingabe
s.listen(1)																#Maximale Anzahl an Verbindungspartnern

quit = False															#Abbruchbedingung
s.setblocking(False)													#Socket soll nicht blockieren --> Kommunikation möglich

name = input("Dein Name: ")												#Der Server wählt einen Chatnamen
name = name + ": "

while quit == False:
	try:
		while True:
		#Verbidnungssocket
			komm, addr = s.accept()										#s.accpet() gibt Tupel mit connection und adresse zurück
			while True:
			#Kommunikationssocket
				data = komm.recv(1024)									#Daten werden empfangen --> Wert in ()?
				if data == "help()":
				    #Abstände checken.
					#nicht print, sondern send
				    print("""\
				    -----------------------------------------------------
				    Help menu:
				    -----------------------------------------------------
				    Commands for the chat:
				        quit() for quitting the chat
				        name() for the name of your communication partner
				        address() for the address of your partner
				    -----------------------------------------------------
				    """)
				elif data == "quit()":									#Beenden der Kommunikation
					quit = True											#evtl durch break ersetzen
					komm.close()
				elif data == "name()":									#Rückgabe gewählter Name des Partner (Server), nicht print() sondern send()
				    #komm.send(name.encode())							#?
				    pass
				elif data == "address":									#Rückgabe des verwendeten Ports, der IP-Adresse und des Hosts
				    #komm.send(addr.encode())							#?
				    pass
				elif data == "":
					pass
				print("[{}]{}".format(addr[0], data.decode()))			#Ausgabe der Nachricht
				message = name + str(input("Antwort: "))				#Typ des Rückgabewerts testen.
				komm.send(message.encode())
	except:
		pass
#finally:
s.close()																#Schließen des Verbindungssockets
print("Server: Server closed.")

#https://docs.python.org/3/library/socket.html#socket.socket.accept
#http://wwwlehre.dhbw-stuttgart.de/~schepper/Vorlesung04.pdf

# wenn data "" ist
