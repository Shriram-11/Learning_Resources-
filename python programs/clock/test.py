import time
import datetime
import playsound
from tkinter import *
def alarm():
	def setime(wakeuptime):
	    while True:
	        time.sleep(1)
	        ct=datetime.datetime.now()
	        rt=ct.strftime("%H:%M:%S")
	        if rt==wakeuptime:
	        	playsound.playsound("sbin.mp3")
	        	break
#speeeeeeeeed and powwwaaaa
	def enter():
		wake=f"{hour.get()}:{mins.get()}:{sec.get()}"
		setime(wake)
	root=Tk()
	root.title('ALARM CLOCK')

	hour=StringVar()
	mins=StringVar()
	sec=StringVar()


	hourTime= Entry(root,textvariable = hour).place(x=100,y=30)
	minTime= Entry(root,textvariable = mins).place(x=130,y=30)
	secTime = Entry(root,textvariable = sec).place(x=160,y=30)

	#To take the time input by user:
	submit = Button(root,text = "Set Alarm",fg="red",width = 10,command = enter).place(x =120,y=70)
	root.mainloop()



alarm()
