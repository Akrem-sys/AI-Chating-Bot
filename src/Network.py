from os import system
from threading import Thread
import socket
from jpysocket import jpydecode,jpyencode

class Network:
    def __init__(self):
        self.host="localhost"
        self.port=12345
    def Connect(self,LookFor):
        s = socket.socket()
        s.connect((self.host, self.port))
        print("Socket Is Connected....")
        msgsend = jpyencode(LookFor)
        s.send(msgsend)
        msgrecv = s.recv(1024)
        msgrecv = jpydecode(msgrecv)

        print("From Server: ", msgrecv)
        s.close()
        print("Connection Closed.")
        return msgrecv
    def RunServer():
        thread=Thread(target=lambda:system("java dicts\\Server.java"))
        thread.daemon=True
        thread.start()