import numpy as np
import matplotlib.pyplot as plt

N = 10  # Number of bits
n = np.random.randint(2, size=N)  # Random bit generation
print("Generated bits:", n)

# Binary to Manchester Conversion
nnn = []  # Initialize list to store Manchester encoded bits
for bit in n:
    if bit == 1:
        nn = [1, -1]  # Manchester encoding for bit 1
    else:
        nn = [-1, 1]  # Manchester encoding for bit 0
    nnn.extend(nn)  # Append Manchester encoded bits to the list

# Manchester Coding Pulse Shaping
i = 0  # Bit index
l = 0.5  # Initial threshold for dividing time into half cycles
t = np.arange(0, N + 0.01, 0.01)  # Time array
y = []  # List to store pulse-shaped Manchester encoded signal
for j in range(len(t)):
    if t[j] <= l:  # Condition for the first half cycle
        y.append(nnn[i])  # Assign values for the first half cycle
    else:
        y.append(nnn[i])  # Assign values for the second half cycle
        i += 1  # Move to the next bit
        l += 0.5  # Update threshold for the next half cycle

# Plotting
plt.plot(t, y, linewidth=2)  # Plot the Manchester encoded signal with linewidth 2
plt.axis([0, N, -1.5, 1.5])  # Set axis limits
plt.grid(True)  # Add grid
plt.title("Manchester Coding")  # Set title
plt.xlabel("Time")  # Label x-axis
plt.ylabel("Amplitude")  # Label y-axis
plt.show()  # Display plot
