import socket
ip = input("IP-Adresse: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))
try:
    name = input("Dein Name: ")
    name = name + ": "
    while True:
        message = input("Nachricht: ")
        message = name + str(message)
        s.send(message.encode())
        antwort = s.recv(1024)
        print("[{}]{}".format(ip, antwort.decode()))
finally:
    s.close()
    print("Server closed.\n")
