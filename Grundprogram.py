import tkinter
from tkinter import * 

root = Tk() 
root.title("CalcPlot")
root.geometry("1570x800")
root.resizable(False,False)
root.configure(bg="grey20")

regn = ""
def show(value):
    global regn
    regn+=value
    res_label.config(text=regn)

def clear(value):
    global regn
    regn = ""
    res_label.config(text=regn)

res_label= Label(root, width=50, height=5, text="", font=("Aptos"), bg="white")
res_label.place(x=60, y=0)

Button(root, text="C", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="red", bg="gray12",command=lambda: clear()).place(x=10, y=100)
Button(root, text="reset", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12",command=lambda: show("/")).place(x=150, y=100)
Button(root, text="/", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=290, y=100)
Button(root, text="x", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=10, y=500)

Button(root, text=".", width=5, height=1, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="gray12").place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="orange").place(x=430, y=400)

root.mainloop()
