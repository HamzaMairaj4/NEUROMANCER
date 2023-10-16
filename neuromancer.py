from tkinter import *

#Define the GUI
def cyberspace():
  neuromancer = Tk()
  neuromancer.title('GPI - NEUROMANCER V3.0.01.3')
  chiba=Canvas(neuromancer,width=500,height=500)
  chiba.pack()
  
  #4 square grid
  chiba.create_line(0,250,500,250)
  chiba.create_line(250,0,250,500)
  
  neuromancer.mainloop()