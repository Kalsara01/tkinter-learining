from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")



def click():
	global myImage
	fileLocation=filedialog.askopenfilename(initialdir="C:/Users/kalsa/Documents/python gui codemy youtube/image",title="open picture", filetypes=(("JPEG files","*.jpg"),("PNG files","*.png"),("all files","*.*")))
	myImage = ImageTk.PhotoImage(Image.open(fileLocation))
	topwindow = Toplevel()
	myLabel=Label(topwindow,image=myImage).pack()

openbtn=Button(root,text="open",command=click).pack()




#loopfn
root.mainloop()