#import json
import socket

f = open("dataset", "a")
soc = socket.socket()


def connect():
    log = open("log", "a")
    #Setting port and IP address
    IP = '127.0.0.1'
    port = 38450
    print("Connection to IP address: %s and Port Number: %s" % (IP, port))
    log.write(
        "Connection to IP address: %s and Port Number: %s \n" % (IP, port))
    #Creating a socket object and binding IP and port
    soc.bind((IP, port))
    log.close()


def recv_msg():
    log = open("log", "a")
    #Setting the serverside to listen to the assigned ports and IP
    soc.listen()
    # Establish connection with client.
    c, addr = soc.accept()
    print("Got connection from %s\n" % (str(addr)))
    log.write("Got connection from %s\n" % (str(addr)))

    msg = soc.recv(1024)
    print(str(msg))
    log.close()
    f.close()


connect()
recv_msg()
