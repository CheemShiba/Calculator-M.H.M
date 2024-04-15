import tkinter
from tkinter import * 

root = Tk() 
root.title("CalcPlot")
root.geometry("1570x800")
root.resizable(False,False)
root.configure(bg="grey20")

res_label= Label(root, width=50, height=5, text="", font=("Aptos"), bg="white")
res_label.place(x=60, y=0)

Button(root, text="C", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dodger blue", bg="black").place(x=10, y=100)
Button(root, text="reset", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=150, y=100)
Button(root, text="/", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=290, y=100)
Button(root, text="x", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=430, y=100)

Button(root, text="7", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=10, y=200)
Button(root, text="8", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=150, y=200)
Button(root, text="9", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=290, y=200)
Button(root, text="-", width=5, height=2, font=("Aptos", 30, "bold"), bd=1, fg="dim gray", bg="dim gray").place(x=430, y=200)

root.mainloop()
