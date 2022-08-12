import os
from tkinter import *
os.system('cls')

root = Tk()
root.title("Calculator")

e = Entry(root, width = 58, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

brojevi = []

def button_click(char):
    brojevi.append(char)
    e.delete(0, END)
    e.insert(0, brojevi)
    
def erase():
    e.delete(0, END)

def equals():
    e.delete(0, END)
    global brojevi
    string_lista = ''.join(brojevi)
    brojevi = []
    evaluate = eval(string_lista)
    e.insert(0, evaluate)

# define buttons

button_open = Button(root, text = "(", padx = 40, pady = 20, command = lambda: button_click("("))
button_close = Button(root, text = ")", padx = 40, pady = 20, command = lambda: button_click(")"))
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click("1"))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click("2"))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click("3"))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click("4"))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click("5"))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click("6"))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click("7"))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click("8"))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click("9"))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click("0"))
button_plus = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_click("+"))
button_minus = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_click("-"))
button_multiply = Button(root, text = "*", padx = 40, pady = 20, command = lambda: button_click("*"))
button_divide = Button(root, text = "/", padx = 40, pady = 20, command = lambda: button_click("/"))
button_equals = Button(root, text = "=", padx = 39, pady = 20, command = equals())
button_dot = Button(root, text = ".", padx = 41, pady = 20, command = lambda: button_click("."))
button_clear = Button(root, text = "C", padx = 85, pady = 20, command = erase())

# place buttons

button_open.grid(row = 1, column =0)
button_close.grid(row = 1, column =1)
button_clear.grid(row = 1, column = 2, columnspan = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_divide.grid(row = 2, column = 3)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_multiply.grid(row = 3, column = 3)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_minus.grid(row = 4, column = 3)

button_dot.grid(row = 5, column = 0)
button_0.grid(row = 5, column = 1)
button_equals.grid(row = 5, column = 2)
button_plus.grid(row = 5, column = 3)


root.mainloop()