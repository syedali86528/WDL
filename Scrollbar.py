#importing tkinter
from tkinter import *
#initalize tkinter
top=Tk()
#setting geometry
top.geometry("250x250")
#setting title
top.title("My Scrollbar")
#creating scroll bar
ab=Scrollbar(top)
ab.pack(side=RIGHT,fill=Y)
#creating listbox
mylist=Listbox(top,yscrollcommand=ab.set)
#giving number to list box
for line in range(30):
	mylist.insert(END,"Number"+str(line))
mylist.pack(side=LEFT)
#attaching number to listbox
ab.config(command=mylist.yview)
#running the mainloop()
mainloop()	
