# Library imports
import numpy as np
import matplotlib.pyplot as plot

# Number of bits
N = 10

# Generate binary bits
n = np.random.randint(2, size=N)
print("Generated binary bits:", n)

# Signal Shaping
i = 1
a = 0
t = np.arange(0, N + 0.01, 0.01)  # Time array with 100 times duration for a single binary bit
y = np.zeros(len(t))  # Initialize signal array

for j in range(len(t)):
    if t[j] >= a and t[j] <= a + 0.5:  # First half of the bit period
        y[j] = n[i - 1]  # Assign bit value
    elif t[j] >= a + 0.5 and t[j] <= i:  # Second half of the bit period
        pass  # No change in signal
    else:
        a += 1  # Move to the next bit period
        i += 1  # Move to the next bit

# Plotting
plot.plot(t, y, linewidth=2)  # Plot the signal with linewidth 2
plot.grid(True)  # Add grid
plot.axis([0, N, -1.5, 1.5])  # Set axis limits
plot.title("Unipolar Return to Zero")  # Set title
plot.xlabel("Time")  # Label x-axis
plot.ylabel("Amplitude")  # Label y-axis
plot.show()  # Display plot
