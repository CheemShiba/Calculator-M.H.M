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
            res_label.config(text="Error")
    else:
        res_label.config(text="")
        
res_label = Label(root, width=30, height=2, text="", font=("Arial", 20), bg="white", fg="black")
res_label.place(x=40, y=0)

Button(root, text="C", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="red", bg="gray12", command=clear).place(x=10, y=100)

Button(root, text="reset", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("reset")).place(x=150, y=100)
Button(root, text="/", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("/")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show("0")).place(x=10, y=500)

Button(root, text=",", width=5, height=1, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="gray12", command=lambda: show(",")).place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("Arial", 30, "bold"), bd=1, fg="dim gray", bg="orange", command=lambda: beregn()).place(x=430, y=400)

root.mainloop()
