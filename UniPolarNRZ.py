import numpy as np
import matplotlib.pyplot as plt

N = 10  # Number of bits
# Generate N random binary bits
n = np.random.randint(2, size=N)
print("Generated binary bits:", n)

# Signal Shaping
i = 1  # Initialize index for binary input data
t = np.arange(0, N + 0.01, 0.01)  # Time array with 100 times duration for a single binary bit
y = np.zeros(len(t))  # Initialize signal array
for j in range(len(t)):
    if t[j] <= i:  # Check if the time is within the duration of the current bit
        y[j] = n[i - 1]  # Assign value from the mapping function
    else:
        y[j] = n[i - 1]  # Assign value from the mapping function for the next bit
        i += 1  # Increment binary input data index for the next bit

# Plotting
plt.plot(t, y, linewidth=2)  # Plot the signal with linewidth 2
plt.axis([0, N, -1.5, 1.5])  # Set axis limits
plt.grid(True)  # Add grid
plt.title('Unipolar NRZ Signaling')  # Set title
plt.xlabel('Time')  # Label x-axis
plt.ylabel('Amplitude')  # Label y-axis
plt.show()  # Display plot
