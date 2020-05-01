from tkinter import *

root = Tk()

##GUI functions
def clickevent1():
	label1=Label(root,text="clicked")
	label1.pack() 

###creating things
btn1=Button(root,text="okay", bg="#006666",fg ="white", padx=50, pady=20, command=clickevent1)
btn2=Button(root,text="cancle", state=DISABLED)


###shoving things to screen
btn1.pack()
btn2.pack()


###just loop the thing
root.mainloop()