from tkinter import *


root = Tk()
root.title("calculator")


## make text box


txtBox = Entry(root,width=25,borderwidth=10,font=("Calibri 20"))
txtBox.grid(row=1,column=1,columnspan=4,padx=5,pady=5) #put it in root

##make a boarder
spacerlabel=Label(root,text=" ")
spacerlabel.grid(row=0,column=0)

#definitions
def button_click(number):
	currentNo = txtBox.get()
	txtBox.delete(0,END)
	txtBox.insert(0,str(currentNo)+str(number))

def Defbutton_clear():
	txtBox.delete(0,END)

def Defbutton_add():
	global Mfunction
	global firstNo
	Mfunction = "add"
	firstNo = txtBox.get()
	txtBox.delete(0,END)

def Defbutton_sub():
	global Mfunction
	global firstNo
	Mfunction = "sub"
	firstNo = txtBox.get()
	txtBox.delete(0,END)

def Defbutton_multi():
	global Mfunction
	global firstNo
	Mfunction = "multi"
	firstNo = txtBox.get()
	txtBox.delete(0,END)

def Defbutton_div():
	global Mfunction
	global firstNo
	Mfunction = "div"
	firstNo = txtBox.get()
	txtBox.delete(0,END)

def Defbutton_equal():
	
	secNo = txtBox.get()
	txtBox.delete(0,END)

	if Mfunction == "add":
		txtBox.insert(0,int(firstNo)+int(secNo)) 

	if Mfunction == "sub":
		txtBox.insert(0,int(firstNo)-int(secNo)) 

	if Mfunction == "multi":
		txtBox.insert(0,int(firstNo)*int(secNo)) 

	if Mfunction == "div":
		if secNo == "0":
			txtBox.insert(0,"You just broke math!")
		else:
			txtBox.insert(0,int(firstNo)/int(secNo)) 



##make buttons
button_1 = Button(root,text="1",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(1))
button_2 = Button(root,text="2",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(2))
button_3 = Button(root,text="3",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(3))
button_4 = Button(root,text="4",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(4))
button_5 = Button(root,text="5",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(5))
button_6 = Button(root,text="6",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(6))
button_7 = Button(root,text="7",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(7))
button_8 = Button(root,text="8",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(8))
button_9 = Button(root,text="9",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=lambda: button_click(9))
button_0 = Button(root,text="0",activebackground="#A8B6FF",padx=150,pady=40,borderwidth=5,command=lambda: button_click(0))
button_add = Button(root,text="+",activebackground="#A8B6FF",padx=40,pady=101,borderwidth=5,command=Defbutton_add)
button_substaract = Button(root,text="-",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=Defbutton_sub)
button_multiply = Button(root,text="X",activebackground="#A8B6FF",padx=40,pady=40,borderwidth=5,command=Defbutton_multi)
button_divide = Button(root,text="/",activebackground="#A8B6FF",padx=41,pady=40,borderwidth=5,command=Defbutton_div)
button_equal = Button(root,text="=",activebackground="#A8B6FF",padx=40,pady=101,borderwidth=5,command=Defbutton_equal)
button_clear = Button(root,text="CC",bg="#FF9259",activebackground="#FF6919",padx=37,pady=40,borderwidth=5,command=Defbutton_clear)



#put things in the grid
spacerlabel2=Label(root,text=" ")
spacerlabel2.grid(row=2,column=1)

#row 1
button_divide.grid(row=3,column=1,padx=3,pady=3)
button_multiply.grid(row=3,column=2,padx=3,pady=3)
button_substaract.grid(row=3,column=3,padx=3,pady=3)
button_clear.grid(row=3,column=4,padx=3,pady=3)

#raw 2
button_7.grid(row=4,column=1,padx=3,pady=3)
button_8.grid(row=4,column=2,padx=3,pady=3)
button_9.grid(row=4,column=3,padx=3,pady=3)
button_add.grid(row=4,column=4,padx=3,pady=3,rowspan=2)

#raw3
button_4.grid(row=5,column=1,padx=3,pady=3)
button_5.grid(row=5,column=2,padx=3,pady=3)
button_6.grid(row=5,column=3,padx=3,pady=3)

#raw4
button_1.grid(row=6,column=1,padx=3,pady=3)
button_2.grid(row=6,column=2,padx=3,pady=3)
button_3.grid(row=6,column=3,padx=3,pady=3)
button_equal.grid(row=6,column=4,padx=3,pady=3,rowspan=2)

#row5
button_0.grid(row=7,column=1,padx=3,pady=3,columnspan=3)

spacerlabel3=Label(root,text=" ")
spacerlabel3.grid(row=8,column=5)



###just loop the thin4
root.mainloop()