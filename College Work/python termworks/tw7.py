# importing main module
from tkinter import *

# root functionalities
root = Tk()
root.title('Calculator')
root.geometry('640x360')

# will house the display
canvas1 = Canvas(root)
canvas1.pack()

# will house the buttons
canvas2 = Canvas(root)
canvas2.pack()

num1 = 0
num2 = 0
# ------------------------------

# functions
def fnInitialize():
	global num1, num2
	num1 = float(entryNum1.get())
	num2 = float(entryNum2.get())

def fnAddNum():
	fnInitialize()
	ans = num1 + num2
	labelAnsVal.config(text = f"Answer: {str(round(ans, 2))}")

def fnSubNum():
	fnInitialize()
	ans = num1 - num2
	labelAnsVal.config(text = f"Answer: {str(round(ans, 2))}")

def fnMulNum():
	fnInitialize()
	ans = num1 * num2
	labelAnsVal.config(text = f"Answer: {str(round(ans, 2))}")

def fnDivNum():
	fnInitialize()
	ans = num1 / num2
	labelAnsVal.config(text = f"Answer: {str(round(ans, 2))}")

# ------------------------------
# widgets

# first number prompt
lablelNum1 = Label(canvas1, text = "Enter num 1:")
lablelNum1.grid(row = 1, column = 1)

# first number will be here
entryNum1 = Entry(canvas1)
entryNum1.grid(row = 1, column = 2)

# second number prompt
lablelNum2 = Label(canvas1, text = "Enter num 2:")
lablelNum2.grid(row = 2, column = 1)

# second number will be here
entryNum2 = Entry(canvas1)
entryNum2.grid(row = 2, column = 2)

# answer prompt
lablelAns = Label(canvas1, text = "Answer")
lablelAns.grid(row = 3, column = 1)

# answer label
labelAnsVal = Label(canvas1)
labelAnsVal.grid(row = 3, column = 2)

# addition button
ButtonAdd = Button(canvas2, text = "Add", command = fnAddNum)
ButtonAdd.grid(row = 1, column = 1)

# subtraction button
ButtonSub = Button(canvas2, text = "Sub", command = fnSubNum)
ButtonSub.grid(row = 1, column = 2)

# multiplication button
ButtonMul = Button(canvas2, text = "Mul", command = fnMulNum)
ButtonMul.grid(row = 2, column = 1)

# division button
ButtonDiv = Button(canvas2, text = "Div", command = fnDivNum)
ButtonDiv.grid(row = 2, column = 2)

# looping trough the program
root.mainloop()
