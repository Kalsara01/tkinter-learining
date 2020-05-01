from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")
#root.geometry("400x400")
my_image1=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/1.jpg"))
my_image2=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/2.png"))
my_image3=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/3.png"))
my_image4=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/4.png"))
my_image5=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/5.png"))

modes=[
"CMV-VC",
"CMV-PC",
"SIMV-VC",
"SIMV-PC",
"Spontanious"
]

modeselection = StringVar()
modeselection.set(modes[0])


def click():
	lbl.configure(text=modeselection.get())
	if modeselection.get()==modes[0]:
		pictframe.configure(image=my_image1)
	elif modeselection.get()==modes[1]:
		pictframe.configure(image=my_image2)
	elif modeselection.get()==modes[2]:
		pictframe.configure(image=my_image3)
	elif modeselection.get()==modes[3]:
		pictframe.configure(image=my_image4)
	elif modeselection.get()==modes[4]:
		pictframe.configure(image=my_image5)
	






dropdown=OptionMenu(root,modeselection,*modes)
dropdown.pack()
btn=Button(root,text="select",command = click).pack()
lbl=Label(root,text="your selection")
lbl.pack()
pictframe=Label(root)
pictframe.pack()

#loopfn
root.mainloop()