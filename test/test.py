import numpy as np

import matplotlib.pyplot as plt

# Generate some mock data
t = np.arange(0.01, 10.0, 0.01)  # Time values from 0.01 to 10.0 with a step of 0.01
data1 = np.exp(t)  # Exponential values based on time
data2 = np.sin(2 * np.pi * t)  # Sine wave values based on time

# Create a figure and axes
fig, ax1 = plt.subplots()

# Plot the first dataset on the first axis
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create a second axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot the second dataset on the second axis
color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Adjust the layout to prevent label clipping
fig.tight_layout()

# Display the plot
plt.show()