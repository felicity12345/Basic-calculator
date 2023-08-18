from tkinter import *
import math
from glob import glob


root = Tk()
root.title("Calculator")

e = Entry(root, width=60, borderwidth=40)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    
    elif math == 'subtraction':
        e.insert(0, f_num - int(second_number))

    elif math == 'multiplication':
        e.insert(0, f_num * int(second_number))

    elif math == 'division':
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math = 'subtraction' 
    f_num = int (first_number)
    e.delete(0, END)
  
def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math = 'multiplication' 
    f_num = int (first_number)
    e.delete(0, END)

def button_divide():
    first_number=e.get()
    global f_num
    global math
    math = 'division' 
    f_num = int (first_number)
    e.delete(0, END)
    
    #def button_operation(operation):
    #global f_num
    #global math
    #math = operation
    #f_num = int(e.get())
    #e.delete(0, END)


# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons and place them on the grid

for button_text, row, col in buttons:
    if button_text == "0":
        Button(root, text=button_text, padx=40, pady=20, command=lambda b=button_text: button_click(b)).grid(row=row, column=col)
    elif button_text == "C":
        Button(root, text=button_text, padx=40, pady=20, command=button_clear).grid(row=row, column=col)
    elif button_text == "=":
        Button(root, text=button_text, padx=100, pady=20, command=button_equal).grid(row=row, column=col, columnspan=2)
    else:
        Button(root, text=button_text, padx=40, pady=20, command=lambda b=button_text: button_click(b)).grid(row=row, column=col)
root.mainloop()
