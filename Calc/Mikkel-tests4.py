##pip install numpy matplotlib


##----------------------------------------------------------------------------
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
##-------------------------------------------------------------------------------------------------

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_number = entry.get()
    global expression
    global math
    math = "addition"
    expression = float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, expression + float(second_number))
    draw_graph()

def draw_graph():
    x = np.linspace(0, 10, 100)
    y = expression * x  # Simple y = mx linear function
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=frame_graph)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    plt.close(fig)

# Adding buttons
button_1 = tk.Button(frame_calculator, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_1.grid(row=1, column=0)

# Add more buttons as needed...

button_add = tk.Button(frame_calculator, text="+", padx=39, pady=20, command=button_add)
button_add.grid(row=4, column=0)

button_equal = tk.Button(frame_calculator, text="=", padx=91, pady=20, command=button_equal)
button_equal.grid(row=4, column=1, columnspan=2)

button_clear = tk.Button(frame_calculator, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=4, column=3)


##----------------------------------------------------------------
root.mainloop()
