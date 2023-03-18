import tkinter as tink
count = -1
run = False
def var_name(mark):
   def RunTimer():
       global hours_timer, minutes_timer, seconds_timer
       if hours_timer == minutes_timer == seconds_timer == 0:
           minutes_timer = 'Time'; seconds_timer = 'up'
           label_timer_hr.grid_forget()
           label_timer_hr_dot.grid_forget()
           label_timer_min_dot.grid_forget()
       elif minutes_timer == seconds_timer == 0:
           hours_timer -=1 
           minutes_timer = seconds_timer = 59
           root.after(1000, RunTimer)
       elif seconds_timer == 0:
           minutes_timer -= 1
           seconds_timer == 59
           root.after(1000, RunTimer)
       else:
           seconds_timer -= 1
           root.after(1000, RunTimer)

       if len(str(seconds_timer)) == 1:
           temp_timer_sec = '0' + str(seconds_timer)
       else:
           temp_timer_sec = str(seconds_timer)
       if len(str(minutes_timer)) == 1:
           temp_timer_min = '0' + str(minutes_timer)
       else:
           temp_timer_min = str(minutes_timer)
       label_timer_hr.config(text = hours_timer)
       label_timer_min.config(text = minutes_timer)
       label_timer_sec.config(text =seconds_timer)
   RunTimer()
# While Running
def Start(mark):
   global run
   run = True
   var_name(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'
# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False
# For Reset
def Reset(label):
   global count
   count = -1
   if run == False:
      reset['state'] = 'disabled'
      mark['text'] = 'Welcome'
   else:
      mark['text'] = 'Start'

base = tink.Tk()
base.title("PYTHON STOPWATCH")
base.minsize(width=300, height=200)
mark = tink.Label(base, text="Welcome", fg="blue", font="Times 25 bold",bg="white")
mark.pack()
start = tink.Button(base, text='Start',width=25, command=lambda: Start(mark))
stop = tink.Button(base, text='Stop', width=25, state='disabled', command=Stop)
reset = tink.Button(base, text='Reset',width=25, state='disabled', command=lambda: Reset(mark))
start.pack()
stop.pack()
reset.pack()
base.mainloop()