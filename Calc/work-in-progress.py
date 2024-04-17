import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Calculator interface
        self.display = tk.Entry(master, width=40, font=('Arial', 18))  # Adjusted for better fit
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=20)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Adjusting button size and padding
        button_height = 4
        button_width = 15
        for (text, row, col) in buttons:
            self.create_button(text, row, col, button_width, button_height)

    def create_button(self, text, row, col, width, height):
        button = tk.Button(self.master, text=text, width=width, height=height,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=10, pady=10)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    root.geometry("800x600")  # Set the window size to 800x600
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
