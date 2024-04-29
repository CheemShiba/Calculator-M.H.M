#python -m pip install -U matplotlib

import matplotlib.pyplot as plt
import numpy as np

# Define the function
def my_function(x):
    return 620*x**3+21

# Generate x values
x_values = np.linspace(-5, 5, 20)  # Generate 100 points between -5 and 5

# Calculate y values using the function
y_values = my_function(x_values)

# Plot the graph
plt.plot(x_values, y_values)
plt.title('Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
