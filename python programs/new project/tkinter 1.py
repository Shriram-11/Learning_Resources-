from tkinter import *
root=Tk()

def fn():
    print('hello word')
somename=Button(root, text='SBIN', command=fn)
somename.pack()

somelabel=Label(root, text='sbinoto')
somelabel.pack()

somentry=Entry(root ,width=30)
somentry.pack()

root.mainloop()
