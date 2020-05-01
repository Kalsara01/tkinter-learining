from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import json
import requests

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")
root.geometry("400x400")


def click():
	global location
	if len(txtbox.get()) == 0:
		messagebox.showerror("no data entry","try again after giving a city name")
	else:
		location=txtbox.get()
		try:
			api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2012d226fe26b7db079e1379281c9aca".format(location))
			api=json.loads(api_request.content)
		except Exception as e:
			api = "error"

		myLabel.configure(text="Tempreture in "+str(api['name'])+" is "+str(api['main']['temp'])+"C")
		#myLabel.configure(text="aa")
		


def refresh():
	try:
		api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2012d226fe26b7db079e1379281c9aca".format(location))
		api=json.loads(api_request.content)
	except Exception as e:
		api = "error"

		
		myLabel.configure(text="Tempreture in "+str(api['name'])+" is "+str(api['main']['temp'])+"C")







txtbox=Entry(root,width=30)
txtbox.grid(row=1,column=1,padx=10,pady=10)
txtboxlbl=Label(root,text="city")
txtboxlbl.grid(row=1,column=0,padx=10,pady=10)
enterbutton=Button(root,text="enter",command=click).grid(row=2,column=0,columnspan=2,ipadx=100,padx=10,pady=10)
refreshbutton=Button(root,text="refresh",command=refresh).grid(row=3,column=0,columnspan=2,ipadx=100,padx=10,pady=10)
myLabel= Label(root, text="")
myLabel.grid(row=4,column=0,columnspan=2,sticky=W)



#loopfn
root.mainloop()