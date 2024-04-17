import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Define the function
def my_function(x):
    return x ** 2

# Generate x values
x_values = np.linspace(-5, 5, 100)  # Generate 100 points between -5 and 5

# Calculate y values using the function
y_values = my_function(x_values)

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib Plot in Tkinter")

# Create a Matplotlib figure
fig = Figure(figsize=(5, 4), dpi=100)

# Add a subplot to the figure
ax = fig.add_subplot(111)
ax.plot(x_values, y_values)
ax.set_title('Graph of y = x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

# Embed the Matplotlib plot into the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Run the Tkinter event loop
tk.mainloop()
