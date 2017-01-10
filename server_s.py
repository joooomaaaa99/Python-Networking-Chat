"""!/usr/bin/python
-*- coding: UTF-8 -*-
Date: 10.01.2017
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#Socket des Moduls Socket wird erstellt
s.bind(("", 100000))										#.bind benötigt Tupel als Eingabe
s.listen(1)													#Maximale Anzahl an Verbindungspartnern

quit = False												#Abbruchbedingung
s.setblocking(False)										#Socket soll nicht blockieren --> Kommunikation möglich

try:
	#Verbidnungssocket
	while quit == False:
		komm, addr = s.accept()								#s.accpet() gibt Tupel mit connection und adresse zurück
		#Kommunikationssocket
		name = input("Dein Name: ")							#Der Server wählt einen Chatnamen
		name = name + ": "
		while True:
			data = komm.recv()								#Daten werden empfangen --> Wert in ()?
			if "help" in str(data):
				#Abstände checken.
				print("""\
				---------------------------------------------------
				Help menu:
				---------------------------------------------------
				Commands for the chat:
					quit() for quitting the chat
					name() for the name of your communication partner
					address() for the address of your partner
				---------------------------------------------------
				""")
			elif "quit()" in str(data):						#Beenden der Kommunikation
				quit = True									#evtl durch break ersetzen
				komm.close()
			elif "name()" in str(data):						#Rückgabe gewählter Name des Partner (Server)
				pass
				#print()
			elif "address()" in str(data):					#Rückgabe des verwendeten Ports, der IP-Adresse und des Hosts
				pass
				#print()
			print("[{}]{}".format(addr[0], data.decode()))	#Ausgabe der Nachricht
			message = name + str(input("Antwort: "))		#Typ des Rückgabewerts testen.
			komm.send(message.encode())
finally:
	s.close()												#Schließen des Verbindungssockets

	
#https://docs.python.org/3/library/socket.html#socket.socket.accept
#http://wwwlehre.dhbw-stuttgart.de/~schepper/Vorlesung04.pdf
