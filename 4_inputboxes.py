from tkinter import *

root = Tk()

entrybox=Entry(root,width=50,borderwidth=5)
entrybox.insert(0,"enter your name",bg="#f55555")

##GUI functions
def clickevent1():
	value = "helow "+ entrybox.get()

	label1=Label(root,text=value)
	label1.pack() 

###creating things
btn1=Button(root,text="okay", bg="#006666",fg ="white", padx=50, pady=20, command=clickevent1)
btn2=Button(root,text="cancle", state=DISABLED)

spacerlabel1=Label(root,text="      ")
spacerlabel2=Label(root,text="      ")

##entry box function


###shoving things to screen
spacerlabel1.pack()
entrybox.pack()
spacerlabel1.pack()
btn1.pack()
btn2.pack()


###just loop the thing
root.mainloop()