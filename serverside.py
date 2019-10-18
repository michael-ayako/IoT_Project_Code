import json
import socket
import time

ip = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log = open("serversidelogs","a")
print("Starting connection")
log.write("Starting connection")
s.bind((ip,port))
log.close()
    
def getmessage():
    log = open("serversidelogs","a")
    print("Listening on %s:%s"%(ip,str(port)))
    log.write("Listening on %s:%s"%(ip,str(port)))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connection establised with %s"%(str(addr)))
        log.write("Listening on %s:%s"%(ip,str(port)))
        dataset = open("dataset","a")
        data = conn.recv(1024)
        dataset.write(str(data))
        conn.send(b"Data recieved")
    log.close



for x in range(10):
    getmessage()
