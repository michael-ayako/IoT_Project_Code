import time
import json
import socket

def log(x):
    logging = open("clientlogs","a")
    print(x)
    logging.write(x+"\n")
    logging.close()


def sensordata():
  sens1 = 1 #Change this line  of code to fit the humidity sensor
  sens2 = 2 #Change this line  of code to fit the humidity sensor
  sens3 = 3 #Change this line  of code to fit the humidity sensor
  sens4 = 4 #Change this line  of code to fit the humidity sensor
  sens5 = 5 #Change this line  of code to fit the humidity sensor
  sens6 = 6 #Change this line  of code to fit the humidity sensor
  sens7 = 7 #Change this line  of code to fit the humidity sensor
  sens8 = 8 #Change this line  of code to fit the humidity sensor
  sens9 = 9 #Change this line  of code to fit the humidity sensor
  rawsensorinfo = {"sensor1":"%s"%(sens1),"sensor2":"%s"%(sens2),"sensor3":"%s"%(sens3),"sensor4":"%s"%(sens4),"sensor5":"%s"%(sens5),"sensor6":"%s"%(sens6),"sensor7":"%s"%(sens7),"sensor8":"%s"%(sens8),"sensor9":"%s"%(sens9)}
  log = open("jsondataset","a")
  log.write(str(rawsensorinfo))
  log.close()
  sensorinfo = json.dumps(rawsensorinfo)
  return bytes(sensorinfo,"utf-8")

def _connect():

  ip = socket.gethostname()
  port = 1234
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip,port))
  s.sendall(sensordata())
  rply = s.recv(1024)
  print(rply.decode("utf-8"))



while(True):
  time.sleep(2)
  _connect()
  
  