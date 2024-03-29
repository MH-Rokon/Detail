import numpy as np
import matplotlib.pyplot as plt

N = 10  # Number of bits to generate

# Bit generating: Generate N random bits (0 or 1)
n = np.random.randint(2, size=N)
print("Generated bits:", n)

# Making data based on bipolar algorithm
nn = np.zeros(N)  # Initialize array to hold bipolar signal
flag = True  # Flag to alternate between positive and negative pulses
for i in range(N):
    if n[i] == 1:
        if flag:
            nn[i] = 1  # Set positive pulse for bit 1
        else:
            nn[i] = -1  # Set negative pulse for bit 1
        flag ^= True  # Toggle flag for next bit

# Signal shaping
i = 1  # Bit index
a = 0  # Pulse starting point
t = np.arange(0, N + 0.01, 0.01)  # Time array with small increments for smooth plotting
y = np.zeros(len(t))  # Output signal array
for j in range(len(t)):
    if t[j] >= a and t[j] <= a + 0.5:  # Positive pulse duration
        y[j] = nn[i - 1]  # Assign amplitude based on bit value
    elif t[j] >= a + 0.5 and t[j] <= i:  # Gap between pulses
        pass  # No signal during this gap
    else:  # Move to the next bit
        a += 1  # Move to the next pulse
        i += 1  # Move to the next bit

# Plotting
plt.plot(t, y, linewidth=2)  # Plot the signal
plt.grid(True)  # Add grid
plt.axis([0, N, -1.5, 1.5])  # Set axis limits
plt.title("Bipolar Return to Zero Encoding")  # Set title
plt.xlabel("Time (bit period)")  # Label x-axis
plt.ylabel("Amplitude")  # Label y-axis
plt.xticks(np.arange(0, N + 1, 1))  # Set x-axis ticks for each bit period
plt.yticks(np.arange(-1, 2, 1))  # Set y-axis ticks for amplitudes -1, 0, 1
plt.show()  # Display plot
