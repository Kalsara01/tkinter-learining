from tkinter import *
from PIL import ImageTk, Image
from tkinter import Frame


root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")
root.geometry("400x400")

resizeframe = Frame(root,width=10,height=10, bd=1, bg="#faa045",relief=SUNKEN)
resizeframe.grid(row=0,column=1, padx=5, pady=5,sticky=NW)

controllerframe = LabelFrame(root,text="sliders")
controllerframe.grid(row=0,column=0,padx=10,pady=10,sticky=N)



def slide(xvalue):
	resizeframe.configure(height=int(xvalue))
	
def click():
	
	yvalue=horizontalslider.get()
	resizeframe.configure(width=int(yvalue))
	


label1=Label(controllerframe,text="vertical value").grid(row=0,column=0,sticky=W)
verticalslider=Scale(controllerframe,from_=0,to=300,resolution=2,length=200,orient=HORIZONTAL,command=slide).grid(row=1,column=0,sticky=W)
label2=Label(controllerframe,text="horizontal value").grid(row=4,column=0,sticky=W)
horizontalslider=Scale(controllerframe, from_=0, to=300, length=200, resolution=2, orient=HORIZONTAL)
horizontalslider.grid(row=5,column=0,sticky=W)
getbtn=Button(root,text="get values",padx=10,pady=10,command=click)
getbtn.grid(row=2,column=0)






#loopfn
root.mainloop()