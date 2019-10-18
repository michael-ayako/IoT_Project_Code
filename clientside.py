import time
import json
import socket

ip = "127.0.0.1"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log = open("clientsidelogs","a")
print("Starting connection")
log.write("Starting connection")
s.connect((ip,port))
log.close()

def sensordata():
  sens1 = 1
  sens2 = 2
  sens3 = 3
  sens4 = 4
  sens5 = 5
  sens6 = 6
  sens7 = 7
  sens8 = 8
  sens9 = 9
  rawsensorinfo = {"sensor1":"%s"%(sens1),"sensor2":"%s"%(sens2),"sensor3":"%s"%(sens3),"sensor4":"%s"%(sens4),"sensor5":"%s"%(sens5),"sensor6":"%s"%(sens6),"sensor7":"%s"%(sens7),"sensor8":"%s"%(sens8),"sensor9":"%s"%(sens9)}
  log = open("jsondataset","a")
  log.write(str(rawsensorinfo))
  log.close()
  sensorinfo = json.dumps(rawsensorinfo)
  return str(sensorinfo).encode()


def _connect():
    s.sendall(sensordata())
    data = s.recv(1024)
    print(repr(data))


for x in range(10):
  _connect()
  time.sleep(5)
  