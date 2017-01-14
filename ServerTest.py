import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50000))
s.listen(1)

try:
    while True:
        komm, addr = a.sccept()
        while True:
            data = komm.recv(1024)
            if not data:
                komm.close()
                break
            print("[{}] {}".format(addr[0], data.decode()))
            nachricht = input("Antwort: ")
            komm.send(nachricht.encode())
finally:
    s.close()
