import sqlite3
import random as randall
import pickle
import pandas as pd
import os
import time
from tkinter import *
from cryptography.fernet import Fernet
import neuromancer
import bootup

#create a table named logins in the specified file
def columbia(fileName):
   conn = sqlite3.connect(fileName)
   c = conn.cursor()
   c.execute('''
             CREATE TABLE IF NOT EXISTS logins
             ([userID] INTEGER PRIMARY KEY,
             [firstName] TEXT,
             [lastName] TEXT,
             [userName] TEXT,
             [password] TEXT)
             ''')

#clear the table in the file specified
def saturnV(fileName):
   conn = sqlite3.connect(fileName)
   c=conn.cursor()
   c.execute('DROP TABLE logins')

#print the whole table in the specified file
def oneSmallStep(fileName,tableName):
   conn = sqlite3.connect(fileName)
   c = conn.cursor()
   conn.commit()
   c.execute('SELECT * FROM '+str(tableName))
   df = pd.DataFrame(c.fetchall(), columns=['userID', 'firstName', 'lastName', 'userName', 'password'])
   return df

#create a new accounut in the specified table using values returned from tkinter input
def armstrong(fileName,tableName,e1,e2,e3,e4):
   conn = sqlite3.connect(fileName)
   c = conn.cursor()
   conn.commit()
   aldrin = c.execute('SELECT * FROM '+tableName)
  
   f=open('nextID','r')
   nextID=f.read()
   f.close()
   userID1=int(nextID)+1
   firstName=e1.get()
   lastName=e2.get()
   userName=e3.get()
   password=e4.get()
   cryptid=galileo(password)
   f=open('orion.pkl','rb')
   orion=pickle.load(f)
   f.close()
   orion={**orion, **cryptid}
   f=open('orion.pkl','wb')
   pickle.dump(orion,f)
   f.close()
   paul=list(cryptid.keys())
   password=paul[0]
   paratrooper=(userID1, firstName, lastName, userName, password)
   c.execute('INSERT INTO logins (userID, firstName, lastName, userName, password) VALUES (?,?,?,?,?)',paratrooper)
   conn.commit()
   f=open('nextID','w')
   f.write(str(userID1))
   f.close()

#Login Function
def aldrin(fileName,tableName,e1,e2):
  conn = sqlite3.connect(fileName)
  c = conn.cursor()
  conn.commit()
  userling=e1.get()
  passling=e2.get()
  c.execute("SELECT * FROM "+tableName+" WHERE userName = ?", (str(userling),))
  discovery = c.fetchone()
  passnerd=atlantis(discovery[-1])
  while passling!=passnerd:
    print('This password is invalid, please try again')
  time.sleep(5)
  os.system('clear')
  bootup.chibaCityBlues('The future is there... looking back at us. Trying to make sense of the fiction we will have become')
  time.sleep(2)
  os.system('clear')
  bootup.overdrive("Welcome, "+discovery[1]+" "+discovery[2]+", to NEUROMANCER")
  neuromancer.cyberspace()

#Login Page
def aldrinV():
  mainframe=Tk()
  mainframe.geometry ("580x500")
  new_page = Toplevel(mainframe)
  label = Label(new_page, text="New Page Content")
  label.pack()
  uset=Label(mainframe,text="Enter username:")
  uset.grid(row=0,column=0)
  past=Label(mainframe,text="Enter password:")
  past.grid(row=1,column=0)
  e1=StringVar()
  userName=Entry(mainframe,textvariable=e1)
  userName.grid(row=0,column=1)
  e2=StringVar()
  password=Entry(mainframe,textvariable=e2)
  password.grid(row=1,column=1)
  avgButton = Button(mainframe, text="Login",command=lambda:aldrin('oregonTrail',
                                                                   'logins'
                                                                   ,userName,password))
  avgButton.grid(row=3,column=0)
  mainframe.mainloop()

#Create Account Page
def armstrongV():
  mainframe=Tk()
  mainframe.geometry ("580x500")
  new_page = Toplevel(mainframe)
  label = Label(new_page, text="New Page Content")
  label.pack()
  
  fst=Label(mainframe,text="Enter your first name:")
  fst.grid(row=0,column=0)
  e1=StringVar()
  firstName=Entry(mainframe,textvariable=e1)
  firstName.grid(row=0,column=1)
  
  lst=Label(mainframe,text="Enter your last name:")
  lst.grid(row=1,column=0)
  e2=StringVar()
  lastName=Entry(mainframe,textvariable=e2)
  lastName.grid(row=1,column=1)

  usr=Label(mainframe,text="Enter your user name:")
  usr.grid(row=2,column=0)
  e3=StringVar()
  userName=Entry(mainframe,textvariable=e3)
  userName.grid(row=2,column=1)

  pswrd=Label(mainframe,text="Enter your password:")
  pswrd.grid(row=3,column=0)
  e4=StringVar()
  password=Entry(mainframe,textvariable=e4)
  password.grid(row=3,column=1)

  avgButton = Button(mainframe, text="Create Account",command=lambda:armstrong('oregonTrail',
                                                                      'logins',firstName,lastName,userName,password))
  avgButton.grid(row=4,column=0)
  mainframe.mainloop()
  print('Account created!')

#Encrypt Password
def galileo(message):
  key= Fernet.generate_key()
  frank = Fernet(key)
  encMessage=frank.encrypt(message.encode())
  return {encMessage:frank}

#Decrypt Password
def atlantis(passling):
  f=open('orion.pkl','rb')
  orion=pickle.load(f)
  f.close()
  decrypted=[]
  for x in orion.items():
    if x[0]==passling:
      frank=x[1]
      return frank.decrypt(passling).decode()