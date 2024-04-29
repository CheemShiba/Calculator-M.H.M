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

        # Entry for function input
        self.func_input = tk.Entry(master, width=40, font=('Arial', 14))
        self.func_input.grid(row=6, column=0, columnspan=5, pady=10)
        self.func_input.insert(0, '2*x + 3')  # Default function

        # Button to update the graph based on the input function
        update_button = tk.Button(master, text="Update Graph", command=self.update_graph)
        update_button.grid(row=7, column=0, columnspan=5)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('reset', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Matplotlib plot
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().grid(row=1, column=4, rowspan=4, padx=20)
        # Initial plot
        self.update_graph()

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
            self.display.delete(0, tk.END)
            self.func_input.delete(0, tk.END)
            self.func_input.insert(0, '2*x + 3')
            self.update_graph()
        else:
            self.display.insert(tk.END, value)

def update_graph(self):
    try:
        # Replace 'x' with '*x' for multiplication, but first ensure it's safe and correct
        expression = self.func_input.get().replace('x', '*x')
        expression = expression.replace('**x', '*x')  # Correct any double multiplication symbols
        
        # Check if the expression is empty or not correctly formatted
        if not expression or 'x' not in expression:
            raise ValueError("Please enter a valid function of 'x'. Example: '2*x + 3'")
        
        x_values = np.linspace(-10, 10, 100)
        y_values = eval(expression)  # Evaluate the expression

        self.ax.clear()
        self.ax.plot(x_values, y_values, color='blue')
        self.ax.set_title('Function: ' + self.func_input.get())
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.grid(True)
        self.fig.canvas.draw()

    except SyntaxError as e:
        self.func_input.delete(0, tk.END)
        self.func_input.insert(0, f"Syntax Error: {str(e)}")
    except Exception as e:
        self.func_input.delete(0, tk.END)
        self.func_input.insert(0, f"Error: {str(e)}")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
