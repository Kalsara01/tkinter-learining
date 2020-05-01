from tkinter import *

root = Tk()

###creating things
myLabel1 = Label(root, text = "heloo")
myLabel2 = Label(root, text= "my name is kalsara")
#just you know you can do all in one step also
mylabel3 = Label(root,text="                ").grid(row=2,column=2)

###shoving things to screen
myLabel1.grid(row=0,column=0)
mylabel3.grid(row=1,column=1)



###just loop the thing
root.mainloop()