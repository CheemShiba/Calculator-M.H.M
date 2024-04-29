import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Calculator interface
        self.display = tk.Entry(master, width=20, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, pady=10)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('reset', 5, 0)  # Reset button in the grid
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Matplotlib plot
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.plot_linear_function()

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().grid(row=1, column=4, rowspan=4, padx=20)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, width=5, height=2,
                           command=lambda text=text: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'reset':
            self.display.delete(0, tk.END)  # Clear the calculator display
            self.plot_linear_function()     # Optionally reset the plot or other components
        else:
            self.display.insert(tk.END, value)

    def plot_linear_function(self):
        x_values = np.linspace(-10, 10, 100)
        y_values = 2 * x_values + 3
        self.ax.clear()
        self.ax.plot(x_values, y_values, color='blue')
        self.ax.set_title('Linear Function: y = 2x + 3')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.grid(True)
        self.fig.canvas.draw()

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
