import json
import socket
import time
import datetime
 


def log(x):
    logging = open("serversidelogs","a")
    print(x)
    logging.write(x+"\n")
    logging.close()

def getmessage():
    conn, addr = s.accept()
    log("Connection successfull to %s"%(str(addr)))
    with conn:
        data = conn.recv(1024)
        str_dataset(data)
        conn.send(bytes("Data received","utf-8"))
        conn.close()

def str_dataset(x):
    dataset = open("dataset","a")
    data = json.loads(x.decode("utf-8"))
    currentDT = str(datetime.datetime.now())
    feeddata = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(currentDT,data['sensor1'],data['sensor2'],data['sensor3'],data['sensor4'],data['sensor5'],data['sensor6'],data['sensor7'],data['sensor8'],data['sensor9'])
    dataset.write(feeddata)
    dataset.close()


ip = socket.gethostname()
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log("Starting connection")
s.bind((ip,port))
log("Listening on %s:%s"%(ip,str(port)))
s.listen()

for x in range(10):
    getmessage()
