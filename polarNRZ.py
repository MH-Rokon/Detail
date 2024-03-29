import numpy as np
import matplotlib.pyplot as plt

N = 10  # Number of bits to generate

# Bit generating: Generate N random bits (0 or 1)
n = np.random.randint(2, size=N)
print("Generated bits:", n)

# Mapping function: Map bits to polar values (-1 or 1)
#The np.where() function maps the bits to polar values (-1 or 1).
nn = np.where(n == 1, 1, -1)

# Signal shaping: Create the polar Non-Return to Zero (NRZ) waveform
i = 1  # Bit index
t = np.arange(0, N + 0.01, 0.01)  # Time array with small increments for smooth plotting
y = np.zeros(len(t))  # Output signal array
for j in range(len(t)):
    if t[j] <= i:  # While within the duration of current bit
        y[j] = nn[i - 1]  # Assign amplitude based on bit value
    else:  # Move to the next bit
        y[j] = nn[i - 1]  # Assign amplitude based on bit value
        i += 1  # Move to the next bit

# Plotting
plt.plot(t, y, linewidth=2)  # Plot the signal
plt.grid(True)  # Add grid
plt.axis([0, N, -1.5, 1.5])  # Set axis limits
plt.title("Polar Non Return to Zero")  # Set title
plt.xlabel("Time")  # Label x-axis
plt.ylabel("Amplitude")  # Label y-axis
plt.show()  # Display plot
