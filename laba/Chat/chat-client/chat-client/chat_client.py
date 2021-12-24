import socket 
import threading
from Shifr import shifr

def read_sok():
    while 1:
        data = sor.recv(1024)
        ddata = data.decode("utf-8")
        a = input("Розшифрувати повідомлення (+/-) ?: ")
        if a == "+":
            print(shifr(key=-1, text=ddata))
        else:
            print(ddata)
server = (("", 2222))
user = input("Enter your name: ")
sor - socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto(shifr(key=1, text=(user + ' Connect to server')).encode('utf-8'), server)
potok = threading.Thread(target= read_sok)
potok.start()
while 1:
    mensahe = input()
    sor.sendto(shifr(key=1, text=("\n" + '[' + user + ']' + mensahe)).encode('utf-8'), server)

