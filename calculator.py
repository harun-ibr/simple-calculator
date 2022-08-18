import os
from math import sqrt
from tkinter import *
os.system('cls')

root = Tk()
root.title("Calculator")

e = Entry(root, width = 20, borderwidth = 2, font = ('Arial 24'))
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 20)

brojevi = []

def get_last_number(lista):
    error = False
    last_number = ''
    while not error and len(lista) > 0:
        try:
            a = int(lista[-1])
            # print(a)
            if isinstance(a, int) or a == ".":
                last_number += str(a)
                lista.pop(-1)
        except:
            if lista[-1] == ".":
                last_number += '.'
                lista.pop(-1)
            else:
                error = True
        # print(last_number)
    lista.append(last_number[::-1])
    # print(lista)
    return lista

def button_click(char):
    brojevi.append(char)
    e.delete(0, END)
    e.insert(0, ''.join(brojevi))
    # print(brojevi)
    
def erase():
    e.delete(0, END)
    global brojevi
    brojevi = []

def equals():
    e.delete(0, END)
    global brojevi
    string_lista = ''.join(brojevi)
    brojevi = []
    evaluate = str(eval(string_lista))
    for i in evaluate:
        brojevi.append(i)
    e.insert(0, ''.join(evaluate))
    # print(brojevi)

def operacija(operation):
    get_last_number(brojevi)
    # print(brojevi)
    if operation == 'korijen':
        rezultat = str(sqrt(float(brojevi[-1])))
    elif operation == 'kvadrat':
        rezultat = str((float(brojevi[-1]))**2)
    elif operation == 'reciprocno':
        rezultat = str(1/(float(brojevi[-1])))
    brojevi.pop(-1)
    for n in rezultat:
        brojevi.append(n)
    e.delete(0, END)
    e.insert(0, ''.join(brojevi))
    # print(f"korjen {brojevi}")
    
def backspace():
    brojevi.pop(-1)
    e.delete(0, END)
    e.insert(0, ''.join(brojevi))
    # print(brojevi)

def percentage():
    global brojevi
    get_last_number(brojevi)
    if len(brojevi) > 1:
        postotak = float(brojevi[-1])
        last_operation = brojevi[-2]
        brojevi.pop(-1)
        brojevi.pop(-1)
        string_lista = ''.join(brojevi)
        brojevi = []
        evaluate = str(eval(string_lista))
        evaluate_float = eval(string_lista)
        for i in evaluate:
            brojevi.append(i)
        brojevi.append(last_operation)
        rezultat = str(postotak/100 * evaluate_float)
        for n in rezultat:
            brojevi.append(n)
        equals()
    else:
        return

def change_sign():
    global brojevi
    get_last_number(brojevi)
    print(brojevi)
    rezultat = float(brojevi[-1])*(-1)
    brojevi.pop(-1)
    sign = ''
    if brojevi[-1] == '+':
        brojevi.pop(-1)
    elif brojevi[-1] == '-':
        brojevi.pop(-1)
        sign = 'minus'
    for i in str(rezultat):
        if sign == 'minus' and i == '-':
            brojevi.append('+')
        else:
            brojevi.append(i)
    e.delete(0, END)
    e.insert(0, ''.join(brojevi))

# define buttons

mc = Button(root, text = "MC", padx = 20, pady = 10)
mr = Button(root, text = "MR", padx = 20, pady = 10)
m_plus = Button(root, text = "M+", padx = 20, pady = 10)
m_minus = Button(root, text = "M-", padx = 20, pady = 10)
ms = Button(root, text = "MS", padx = 20, pady = 10)
m_list = Button(root, text = "M?", padx = 20, pady = 10)

button_percentage = Button(root, text = "%", padx = 40, pady = 20, command = percentage)
clear_e = Button(root, text = "CE", padx = 40, pady = 20, command = erase)
clear = Button(root, text = "C", padx = 41, pady = 20, command = erase)
delete = Button(root, text = "<-x-", padx = 40, pady = 20, command = backspace)

one_ove_x = Button(root, text = "1/x", padx = 40, pady = 20, command = lambda: operacija('reciprocno'))
x_squared = Button(root, text = "x^2", padx = 40, pady = 20, command = lambda: operacija('kvadrat'))

open = Button(root, text = "(", padx = 80, pady = 20, command = lambda: button_click("("))
close = Button(root, text = ")", padx = 80, pady = 20, command = lambda: button_click(")"))

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

plus = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_click("+"))
minus = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_click("-"))
multiply = Button(root, text = "*", padx = 40, pady = 20, command = lambda: button_click("*"))
divide = Button(root, text = "/", padx = 40, pady = 20, command = lambda: button_click("/"))
button_equals = Button(root, text = "=", padx = 39, pady = 20, command = equals)
dot = Button(root, text = ".", padx = 41, pady = 20, command = lambda: button_click("."))
plus_minus = Button(root, text = "+/-", padx = 41, pady = 20, command = change_sign)
button_sqrt = Button(root, text = "√", padx = 41, pady = 20, command = lambda: operacija('korijen'))

# button_test = Button(root, text = "test", padx = 85, pady = 20, command = lambda: get_last_number(brojevi))

# place buttons

# mc.grid(row = 1, column = 0, sticky = 'ew')
# mr.grid(row = 1, column = 1)
# m_plus.grid(row = 1, column = 2)
# m_minus.grid(row = 1, column = 3)
# ms.grid(row = 1, column = 4)
# m_list.grid(row = 1, column = 5)

button_percentage.grid(row = 2, column = 0, sticky = 'ew')
clear_e.grid(row = 2, column = 1, sticky = 'ew')
clear.grid(row = 2, column = 2, sticky = 'ew')
delete.grid(row = 2, column = 3, sticky = 'ew')

one_ove_x.grid(row = 3, column = 0, sticky = 'ew')
x_squared.grid(row = 3, column = 1, sticky = 'ew')
button_sqrt.grid(row = 3, column = 2, sticky = 'ew')
divide.grid(row = 3, column = 3, sticky = 'ew')

button_7.grid(row = 4, column = 0, sticky = 'ew')
button_8.grid(row = 4, column = 1, sticky = 'ew')
button_9.grid(row = 4, column = 2, sticky = 'ew')
multiply.grid(row = 4, column = 3, sticky = 'ew')

button_4.grid(row = 5, column = 0, sticky = 'ew')
button_5.grid(row = 5, column = 1, sticky = 'ew')
button_6.grid(row = 5, column = 2, sticky = 'ew')
minus.grid(row = 5, column = 3, sticky = 'ew')

button_1.grid(row = 6, column = 0, sticky = 'ew')
button_2.grid(row = 6, column = 1, sticky = 'ew')
button_3.grid(row = 6, column = 2, sticky = 'ew')
plus.grid(row = 6, column = 3, sticky = 'ew')

plus_minus.grid(row = 7, column = 0, sticky = 'ew')
button_0.grid(row = 7, column = 1, sticky = 'ew')
dot.grid(row = 7, column = 2, sticky = 'ew')
button_equals.grid(row = 7, column = 3, sticky = 'ew')


open.grid(row = 8, column = 0, columnspan = 2, sticky = 'ew')
close.grid(row = 8, column = 2, columnspan = 2, sticky = 'ew')

# button_test.grid(row = 7, column = 1)

root.mainloop()