import socket
ip = input("IP-Adresse: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))
name = input("Dein Name: ")
name = name + ": "
try:
    while True:
        message = input("Antwort: ")
        message = name + str(message)
        s.send(message.encode())
        antwort = s.recv(1024)
        print("[{}]{}".format(ip, antwort.decode()))
finally:
    s.close()
    print("Client: Server closed.\n")
