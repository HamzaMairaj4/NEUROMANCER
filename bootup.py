import os
import time

def startup():
  for x in range(5):
    print("Booting.")
    time.sleep(0.5)
    os.system('clear')
    print("Booting..")
    time.sleep(0.5)
    os.system('clear')
    print("Booting...")
    time.sleep(0.5)
    os.system('clear')

def overdrive(msg):
  sr=""
  for x in msg:
    os.system('clear')
    sr+=x
    print(sr)
    time.sleep(0.05)
    if len(sr)!=len(msg):
      pass
    else:
      break

def chibaCityBlues(msg):
  startup()
  overdrive(msg)