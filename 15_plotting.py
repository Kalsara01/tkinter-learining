from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np 
import matplotlib.pyplot as plt

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")
root.geometry("400x400")


houseprices=np.random.normal(2000000,2500,50000)

def graph():
	plt.hist(houseprices,200)
	plt.show()

btn=Button(root,text="click",command=graph).pack()



#loopfn
root.mainloop()