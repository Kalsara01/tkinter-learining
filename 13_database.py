from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/kalsa/Documents/python gui codemy youtube/icon_0m1_icon.ico")
root.geometry("400x700")

#database

#step 1 - create a database or make a batabase
db1=sqlite3.connect('address_book.db')

#step 2 - make a cursor // a communicator to do stuff
MyCursor = db1.cursor()

#step 3 - setup a table
#MyCursor.execute(""" CREATE TABLE addresses (
#	first_name text,
#	last_name text,
#	address text,
#	city text,
#	state text,
#	zipcode integer
#	)""")

def clickSubmit():
	#step 1 - create a database or make a batabase
	db1=sqlite3.connect('address_book.db')

	#step 2 - make a cursor // a communicator to do stuff
	MyCursor = db1.cursor()

	#step 3 
	MyCursor.execute("INSERT INTO addresses VALUES (:fname,:lname,:address,:city,:state,:zipcode)",
			{
				'fname': fname.get(),
				'lname': lname.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get()
			}
		)



	#step 4 - send what ever the daa
	db1.commit()

	#step5 - end connection
	db1.close()

	#cler feilds
	fname.delete(0,END)
	lname.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)



def fetch():
	#step 1 - create a database or make a batabase
	db1=sqlite3.connect('address_book.db')

	#step 2 - make a cursor // a communicator to do stuff
	MyCursor = db1.cursor()
	
	MyCursor.execute("SELECT *, oid FROM addresses")
	dbrecods=MyCursor.fetchall()
	#print(dbrecods)

	
	print_recods = ""
	for recods in dbrecods:
		print_recods += str(recods[6])+ "\t" + str(recods[0])+ "\n"

	outputlbl.configure(text=print_recods)



	#step 4 - send what ever the daa
	db1.commit()

	#step5 - end connection
	db1.close()
	

def delete():
	#step 1 - create a database or make a batabase
	db1=sqlite3.connect('address_book.db')

	#step 2 - make a cursor // a communicator to do stuff
	MyCursor = db1.cursor()

	MyCursor.execute("DELETE from addresses WHERE oid = " + deletebox.get())

	deletebox.delete(0,END)
	MyCursor.execute("SELECT *, oid FROM addresses")
	dbrecods=MyCursor.fetchall()
	print_recods = ""
	for recods in dbrecods:
		print_recods += str(recods[6])+ "\t" + str(recods[0])+ "\n"

	outputlbl.configure(text=print_recods)

	#step 4 - send what ever the daa
	db1.commit()

	#step5 - end connection
	db1.close()





#create some labesls and text boxes
fnamelbl=Label(root,text = "first name", padx=10,pady=10)
fnamelbl.grid(row=0,column=0,sticky=W)
lnamelbl=Label(root,text = "last name", padx=10,pady=10)
lnamelbl.grid(row=1,column=0,sticky=W)
addresslbl=Label(root,text = "address", padx=10,pady=10)
addresslbl.grid(row=2,column=0,sticky=W)
citylbl=Label(root,text = "city", padx=10,pady=10)
citylbl.grid(row=3,column=0,sticky=W)
statelbl=Label(root,text = "state", padx=10,pady=10)
statelbl.grid(row=4,column=0,sticky=W)
ziplbl=Label(root,text = "zip code", padx=10,pady=10)
ziplbl.grid(row=5,column=0,sticky=W)
deletelbl=Label(root,text = "delete id", padx=10,pady=10)
deletelbl.grid(row=8,column=0,sticky=W)


fname=Entry(root,width=30)
fname.grid(row=0,column=1)
lname=Entry(root,width=30)
lname.grid(row=1,column=1)
address=Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)
deletebox=Entry(root,width=30)
deletebox.grid(row=8,column=1)

btnSubmit=Button(root,text="submit",command=clickSubmit)
btnSubmit.grid(row=6,column=0,columnspan=2,padx=10,pady=25,ipadx=125)

btncallback = Button(root,text="call back",command=fetch)
btncallback.grid(row=7, column=0,columnspan=2,padx=10,pady=5,ipadx=120)

btndelete = Button(root,text="delete",command=delete)
btndelete.grid(row=9, column=0,columnspan=2,padx=10,pady=5,ipadx=120)

outputlbl=Label(root,text="")
outputlbl.grid(row=10,column=0,columnspan=2)

#step 4 - send what ever the daa
db1.commit()

#step5 - end connection
db1.close()



#loopfn
root.mainloop()