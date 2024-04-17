import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main window
root = tk.Tk()
root.title("Simple Calculator with Graph")

# Define frame for Calculator
frame_calculator = tk.Frame(root, padx=5, pady=5)
frame_calculator.grid(row=0, column=0, sticky="nsew")

# Define frame for Graph
frame_graph = tk.Frame(root, padx=5, pady=5)
frame_graph.grid(row=0, column=1, sticky="nsew")

# Variable to hold the expression
expression = ""

# Entry widget to show calculations
entry = tk.Entry(frame_calculator, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_operation(operator):
    first_number = entry.get()
    global expression
    global math
    math = operator
    expression = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    try:
        if math == "addition":
            result = expression + float(second_number)
        elif math == "subtraction":
            result = expression - float(second_number)
        elif math == "multiplication":
            result = expression * float(second_number)
        elif math == "division":
            result = expression / float(second_number)
        entry.insert(0, result)
        draw_graph(result)
    except Exception as e:
        entry.insert(0, "Error")
        print("Error:", e)

def draw_graph(coefficient):
    x = np.linspace(0, 10, 100)
    y = coefficient * x  # Simple y = mx linear function
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    plt.close(fig)

# Numeric Buttons
for i in range(1, 10):
    button = tk.Button(frame_calculator, text=str(i), padx=40, pady=20, command=lambda i=i: button_click(i))
    row = (i-1)//3 + 1
    column = (i-1)%3
    button.grid(row=row, column=column)

button_0 = tk.Button(frame_calculator, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_0.grid(row=4, column=1)

# Operation Buttons
button_add = tk.Button(frame_calculator, text="+", padx=39, pady=20, command=lambda: button_operation("addition"))
button_subtract = tk.Button(frame_calculator, text="-", padx=41, pady=20, command=lambda: button_operation("subtraction"))
button_multiply = tk.Button(frame_calculator, text="*", padx=41, pady=20, command=lambda: button_operation("multiplication"))
button_divide = tk.Button(frame_calculator, text="/", padx=41, pady=20, command=lambda: button_operation("division"))

button_add.grid(row=4, column=0)
button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

# Equal and Clear Buttons
button_equal = tk.Button(frame_calculator, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(frame_calculator, text="Clear", padx=79, pady=20, command=button_clear)
button_equal.grid(row=4, column=2, columnspan=2)
button_clear.grid(row=5, column=3)

root.mainloop()
