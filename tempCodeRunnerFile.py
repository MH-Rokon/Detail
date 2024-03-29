import numpy as np
import matplotlib.pyplot as plt

# Binary information at transmitter
x = np.array([1, 0, 1, 0, 1, 0, 1, 0])
bp = 0.000001
print('Binary Information at transmitter:')
print(x)

# Representation of Transmitting binary information as digital signal
bit = np.concatenate([np.ones(100) if bit_value == 1 else np.zeros(100) for bit_value in x])
# Concatenate sequences of ones and zeros to create the digital signal
t1 = np.arange(bp / 100, 100 * len(x) * (bp / 100) + bp / 100, bp / 100)
# Generate time array for the digital signal

# Binary FSK Modulation
A = 5  # Amplitude of the carrier signal
br = 1 / bp  # Bit rate (bits per second)
f1, f2 = br * 8, br * 2  # Frequencies for FSK modulation
t2 = np.arange(bp / 99, bp + bp / 99, bp / 99)  # Time array for carrier signal
m = np.concatenate([A * np.cos(2 * np.pi * f1 * t2) if bit_value == 1 else A * np.cos(2 * np.pi * f2 * t2) for bit_value in x])
# Generate FSK modulated signal based on binary information
t3 = np.arange(bp / 99, bp * len(x) + bp / 99, bp / 99)
# Time array for modulated signal

# Plotting
plt.subplot(311)
plt.plot(t1, bit, linewidth=2.5)
# Plot digital signal
plt.grid(True)
plt.axis([0, bp * len(x), -0.5, 1.5])
plt.ylabel('Amplitude (volt)')
plt.xlabel('Time (sec)')
plt.title('Transmitting Information as Digital Signal')

plt.subplot(312)
plt.plot(t3, m)
# Plot FSK modulated signal
plt.grid(True)
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude (volt)')
plt.title('Waveform for binary FSK Modulation Corresponding Binary Information')

plt.tight_layout()
plt.show()
