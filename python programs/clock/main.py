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







def clock():
	root=Tk()
	root.title('CLOCK')
	def t():
		ct= datetime.datetime.now()
		rt= ct.strftime("%H:%M:%S")
		label.config(text=rt)
		label.after(1000,t)
	label=Label(root,background='white',foreground='black')
	label.pack()
	t()
	mainloop()






def stopwatch():
   start=time.time()
   pre=start
   lap=1  
   try:
      while True:
         input() #press enter to start or to start a new lap
         rounds=round((time.time() - pre), 2)   #current time-previous time =time taken
         net=round((time.time() - start), 2)    #current time - time at which stop watch started 
         print("Lap No. ",str(lap))
         print("Lap Time: ",str(rounds))
         print("Total Time: ",str(net))
         pre=time.time()
         lap+=1
   except KeyboardInterrupt:  #once you press ctrl+c the stop watch is terminated
      print(net)



