from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")

my_image=ImageTk.PhotoImage(Image.open("G:/PHOTOS/orion/d7000a/3.jpg"))
my_imagelablel=Label(root,image=my_image)
my_imagelablel.pack()





#loopfn
root.mainloop()