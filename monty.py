# from tkinter import *

f=open('orion.pkl','wb')
g={}
pickle.dump(g,f)
f.close()

# mainframe = Tk()
# mainframe.geometry ("500x500")

# def getAverage(a,b,c):
#   sum = float(scoreEntry1.get()) + float(scoreEntry2.get()) + float(scoreEntry3.get())
#   average=sum/3.0
#   calcAverageLabel = Label(mainframe,text="%.2f"%average)
#   calcAverageLabel.grid(row=4, column=1)

# #Add label wigits
# score1=Label(mainframe,text="Enter score for test 1:")
# score1.grid(row=0,column=0)
# score2=Label(mainframe,text="Enter score for test 2:")
# score2.grid(row=1,column=0)
# score3=Label(mainframe,text="Enter score for test 3:")
# score3.grid(row=2,column=0)
# averageLabel=Label(mainframe,text="The Average is:")
# averageLabel.grid(row=4,column=0)

# #Entry Widgets
# e1=IntVar()
# e2=IntVar()
# e3=IntVar()
# scoreEntry1=Entry(mainframe,textvariable=e1)
# scoreEntry1.grid(row=0,column=1)
# scoreEntry2=Entry(mainframe,textvariable=e2)
# scoreEntry2.grid(row=1,column=1)
# scoreEntry3=Entry(mainframe,textvariable=e3)
# scoreEntry3.grid(row=2,column=1)

# #Button Widget
# avgButton = Button(mainframe, text="Average",command=lambda:getAverage(scoreEntry1,scoreEntry2,scoreEntry3))
# avgButton.grid(row=3,column=0)

# #Quit button
# quitButton = Button(mainframe, text="Quit",command=mainframe.destroy)
# quitButton.grid(row=3,column=1)

# mainframe.mainloop()