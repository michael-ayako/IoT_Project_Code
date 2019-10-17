import time
import json
import socket
time.sleep(2)

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
  sensorinfo = json.dumps(rawsensorinfo)
  return b"MSG",sensorinfo

for x in range(10):
  IP = '127.0.0.1'
  port = 38450
  soc = socket.socket()
  soc.connect((IP,port))
  soc.send(sensordata())
  