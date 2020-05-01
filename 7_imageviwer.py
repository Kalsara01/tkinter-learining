from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")

my_image1=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/1.jpg"))
my_image2=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/2.png"))
my_image3=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/3.png"))
my_image4=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/4.png"))
my_image5=ImageTk.PhotoImage(Image.open("C:/Users/kalsa/Documents/python gui codemy youtube/image/5.png"))

myImageList=[my_image1,my_image2,my_image3,my_image4,my_image5]


my_imagelablel=Label(image=myImageList[0])
my_imagelablel.grid(row=0,column=0,columnspan=3)


fbtnstatus=ACTIVE
bbtnstatus=ACTIVE
global imgnumber
imgnumber=0

mystatuslbl=Label(root,text="Image " + str(imgnumber + 1)+" out of "+str(len(myImageList)),bd=2,relief=SUNKEN,anchor=E).grid(row=2,column=0,sticky=W+E,columnspan=3)


def fbtnclick():
		
	global imgnumber
	global my_imagelablel
	imgnumber += 1
	backBtn.configure(state=ACTIVE)
	my_imagelablel.grid_forget()
	my_imagelablel=Label(image=myImageList[imgnumber])
	my_imagelablel.grid(row=0,column=0,columnspan=3)
	mystatuslbl=Label(root,text="Image " + str(imgnumber + 1)+" out of "+str(len(myImageList)),bd=2,relief=SUNKEN,anchor=E).grid(row=2,column=0,columnspan=3,sticky=W+E)

	
	if imgnumber == 4:
		fowardBtn.configure(state=DISABLED)
		backBtn.configure(state=ACTIVE)
	elif imgnumber != 4:
		fowardBtn.configure(state=ACTIVE)



	

def bbtnclick():
	global imgnumber
	global my_imagelablel
	imgnumber -= 1

	if imgnumber == 0:
		backBtn.configure(state=DISABLED)
	else:
		backBtn.configure(state=ACTIVE)

	fowardBtn.configure(state=ACTIVE)

	my_imagelablel.grid_forget()
	my_imagelablel=Label(image=myImageList[imgnumber])
	my_imagelablel.grid(row=0,column=0,columnspan=3)
	mystatuslbl=Label(root,text="Image " + str(imgnumber + 1)+" out of "+str(len(myImageList)),bd=2,relief=SUNKEN,anchor=E).grid(row=2,column=0,sticky=W+E,columnspan=3)
	

#
#print (imgnumber)

exitBtn = Button(root,text="exit",command=root.quit)
fowardBtn = Button(root,text=">>",padx=50,command=fbtnclick)
backBtn = Button(root,text="<<",padx=50,state=DISABLED,command=bbtnclick)

exitBtn.grid(row=1,column=1,pady=10)
fowardBtn.grid(row=1,column=2)
backBtn.grid(row=1,column=0)


#loopfn
root.mainloop()