import tkinter as tk
from tkinter import *
import numpy as np
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import font as tkFont

root = Tk()
root.title("CalcPlot")
root.geometry("1550x800")
root.resizable(False, False)
root.configure(bg="grey20")

regn = ""
def show(value):
    global regn
    regn += value
    res_label.config(text=regn)

def clear():
    global regn
    regn = ""
    res_label.config(text=regn)

def beregn():
    global regn
    if regn != "":
        try:
            result = eval(regn)
            regn = str(result)
            res_label.config(text=result)
        except:
            regn = ""
            res_label.config(text="Fejl")
    else:
        res_label.config(text="")

def update_graph():
    try:
        safe_dict = {
            'x': np.linspace(-10, 10, 400),
            'np': np,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'exp': math.exp,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi
        }
        expression = func_input.get().replace('^', '**')
        y_values = eval(expression, {"__builtins__": None}, safe_dict)

        ax.clear()
        ax.plot(safe_dict['x'], y_values, color='blue')
        ax.set_title('Funktion: ' + func_input.get())
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        fig.canvas.draw()
    except Exception as e:
        func_input.delete(0, tk.END)
        func_input.insert(0, f"ugyldig funktion: {str(e)}")

def clear_grafentry():
    func_input.delete(0, tk.END)

def reset_graf():
    ax.clear()  
    fig.canvas.draw()

res_label = Label(root, width=30, height=2, text="", font=("Arial", 20), bg="white", fg="black")
res_label.place(x=40, y=10)

kursiv = tkFont.Font(family="Broadway", size=90, slant="italic")

logo = Label(root, text="CalcPlot", font=kursiv,bg="grey20",fg="white") 
logo.place(x=10,y=610)

func_input = Entry(root, width=15, font=("Arial", 30), bg="white", fg="black", justify=tk.CENTER)
func_input.place(x=900, y=720)
func_input.insert(0, '2*x + 3')

update_button = Button(root, text="Opdater graf",width=13, height=2, font=("Arial", 20, "bold"), bd=1, fg="dim gray", bg="gray12", command=update_graph)
update_button.place(x=620, y=700)

cleargraf = Button(root, text="clear",width=13, height=2, font=("Arial", 20, "bold"), bd=1, fg="dim gray", bg="gray12", command=clear_grafentry)
cleargraf.place(x=1290, y=700)

buttonc = Button(root, text="C", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="red", bg="gray12", command=clear).place(x=10, y=100)

resetgraf = Button(root, text="reset", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=reset_graf).place(x=150, y=100)

buttondevidere = Button(root, text="/", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("/")).place(x=290, y=100)
buttongange = Button(root, text="*", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("*")).place(x=430, y=100)

button7 = Button(root, text="7", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("7")).place(x=10, y=200)
button8 = Button(root, text="8", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("8")).place(x=150, y=200)
button9 = Button(root, text="9", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("9")).place(x=290, y=200)
buttonminus = Button(root, text="-", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("-")).place(x=430, y=200)

button4 = Button(root, text="4", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("4")).place(x=10, y=300)
button5 = Button(root, text="5", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("5")).place(x=150, y=300)
button6 = Button(root, text="6", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("6")).place(x=290, y=300)
buttonplus = Button(root, text="+", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("+")).place(x=430, y=300)

button1 = Button(root, text="1", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("1")).place(x=10, y=400)
button2 = Button(root, text="2", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("2")).place(x=150, y=400)
button3 = Button(root, text="3", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("3")).place(x=290, y=400)
button0 = Button(root, text="0", width=11, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("0")).place(x=10, y=500)

buttonpunktum = Button(root, text=".", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show(".")).place(x=290, y=500)
buttonligmed = Button(root, text="=", width=5, height=3, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="orange", command=lambda: beregn()).place(x=430, y=400)

fig = Figure(figsize=(6, 4.5), dpi=150)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=620, y=10)

root.mainloop()