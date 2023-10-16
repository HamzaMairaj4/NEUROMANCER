import os
import time

#Write "Booting..." in the console to let user know code is still working
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

#Write a message for gravitas
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

#Write a message for gravitas after booting up
def chibaCityBlues(msg):
  startup()
  overdrive(msg)