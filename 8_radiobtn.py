from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")

frame1=LabelFrame(root,text="Pizza Types",padx=10, pady=10)
frame1.grid(row=0,column=0, padx=10,pady=10)

PizzaTypes = [
("pepperoni","type1"),
("chesse","type2"),
("chicken","type3"),
("mushroom","type4"),
("pinapple","type5")
]

typeofpizza = StringVar()
typeofpizza.set("")


	

for nameofpizza, codename in PizzaTypes:
	Radiobutton(frame1,text=nameofpizza,variable=typeofpizza,value=codename,tristatevalue="x").pack(anchor=W)


def click():
	aa=typeofpizza.get()
	mylabel=Label(root,text=aa).grid(row=2,column=0,padx=10,pady=10)
	
	


btn1=Button(root,text="select",command=click).grid(row=1,column=0,padx=10,pady=10)




#loopfn
root.mainloop()