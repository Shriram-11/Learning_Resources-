import sys
from Tkinter import *
from threading import Timer
# a boolean for telling the timer to stop
stop_timer = False

mgui = Tk()

def work(var):
    # stop_timers sets to True or False with Start/Stop
    stop_timer = var
    # work_done will evaluate if timer should start or be canceled
    def work_done(var2):
        stop_timer = var2
        # if stop was pressed t.start() will be ignored
        if stop_timer == False:
            t.start()
        # if stop was pressed timer will stop
        if stop_timer == True:
            print("Stopped!")
            t.cancel()
    t = Timer(1, work, [False])
    print ("Something")
    work_done(var)

mgui.geometry('450x450')
mgui.title('Test')

cmd1 = lambda: work(False)
btn = Button(mgui, text="Start", command =cmd1).place(x=50, y=50)
cmd2 = lambda: work(True)
btn2 = Button(mgui, text="Stop", command =cmd2).place(x=100, y=50)

mgui.mainloop()