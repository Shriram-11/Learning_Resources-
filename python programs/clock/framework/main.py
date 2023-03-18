import time
import datetime
import playsound
import tkinter


def alarm(wakeuptime):
   while True:
       time.sleep(1)
       ct= datetime.datetime.now()   #current date and time
       rt= ct.strftime("%H:%M:%S")  #current time
       if rt==wakeuptime:
          playsound.playsound("sbin.mp3")
          break




def clock():
   while True:
      time.sleep(1)
      ct= datetime.datetime.now()
      rt= ct.strftime("%H:%M:%S")
      print(rt)


def stopwatch():
   start=time.time()
   pre=start
   lap=1  
   try:
      while True:
         input() #press enter to start a new lap else press ctrl+c to end it without moving to next lap
         rounds=round((time.time() - pre), 2)   #current time-previous time =time taken
         net=round((time.time() - start), 2)    #current time - time at which stop watch started 
         print("Lap No. ",str(lap))
         print("Lap Time: ",str(rounds))
         print("Total Time: ",str(net))
         pre=time.time()
         lap+=1
   except KeyboardInterrupt:  #once you press ctrl+c the stop watch is terminated
      net=round((time.time() - start), 2) 
      print(net)


stopwatch()
