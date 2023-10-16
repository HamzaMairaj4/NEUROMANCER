import sqlite3
import pandas as pd
import forAllMankind
from tkinter import *
from cryptography.fernet import Fernet
import pickle
import bootup

#Create the login window
loki = Tk()
loki.title("GPI - NEUROMANCER V3.01.3")
loki.geometry ("580x500")
canvas = Canvas(loki, width=580, height=500)
canvas.pack()
rgb_color=(52,53,65)
canvas.create_polygon(0, 0, 500, 500, 0, 500, fill='#%02x%02x%02x' % rgb_color)
rgb_color=(52,53,85)
canvas.create_line(50,0,550,500,width=2,fill='#%02x%02x%02x' % rgb_color)
rgb_color=(230,230,240)
canvas.create_polygon(580, 0, 580, 250, 330, 0, fill='#%02x%02x%02x' % rgb_color)

#Login Widget
loginButton= Button(loki, text="Login",font=("Palatino",16), width=4,height=1,command=lambda:forAllMankind.aldrinV())
loginButton.place(x=200,y=190)

#Create account button
createAcctButton = Button(loki, text="Create Account",font=("Palatino",16), width=12,height=1,command=lambda:forAllMankind.armstrongV())
createAcctButton.place(x=200,y=250)

loki.mainloop()




















