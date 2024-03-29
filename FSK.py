import numpy as np
import matplotlib.pyplot as plt

# Binary information at transmitter
x = np.array([1, 0, 1, 0, 1, 0, 1, 0])  # Binary sequence to be transmitted
bp = 0.000001  # Time duration of one bit (1 microsecond)
print('Binary Information at transmitter:')
print(x)

# Representation of Transmitting binary information as digital signal
bit = np.concatenate([np.ones(100) if bit_value == 1 else np.zeros(100) for bit_value in x])
# Each bit represented by a sequence of 100 samples
t1 = np.arange(bp / 100, 100 * len(x) * (bp / 100) + bp / 100, bp / 100)  # Time array for digital signal

# Binary FSK Modulation
A = 5  # Amplitude of the carrier signal
br = 1 / bp  # Bit rate (bits per second)
f1, f2 = br * 8, br * 2  # Frequencies for binary FSK modulation
t2 = np.arange(bp / 99, bp + bp / 99, bp / 99)  # Time array for carrier signal
m = np.concatenate([A * np.cos(2 * np.pi * f1 * t2) if bit_value == 1 else A * np.cos(2 * np.pi * f2 * t2) for bit_value in x])
# FSK modulation: Modulating binary signal with carrier wave
t3 = np.arange(bp / 99, bp * len(x) + bp / 99, bp / 99)  # Time array for modulated signal

# Plotting
plt.subplot(311)  # Subplot for digital signal
plt.plot(t1, bit, linewidth=2.5)  # Plot digital signal
plt.grid(True)  # Add grid
plt.axis([0, bp * len(x), -0.5, 1.5])  # Set axis limits
plt.ylabel('Amplitude (volt)')  # Label y-axis
plt.xlabel('Time (sec)')  # Label x-axis
plt.title('Transmitting Information as Digital Signal')  # Set title

plt.subplot(312)  # Subplot for modulated signal
plt.plot(t3, m)  # Plot modulated signal
plt.grid(True)  # Add grid
plt.xlabel('Time (sec)')  # Label x-axis
plt.ylabel('Amplitude (volt)')  # Label y-axis
plt.title('Waveform for binary FSK Modulation Corresponding Binary Information')  # Set title

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()  # Display plot
