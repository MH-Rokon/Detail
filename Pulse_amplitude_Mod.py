import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 20  # Carrier frequency (Hz)
fm = 2   # Modulating frequency (Hz)
fs = 1000  # Sampling frequency (Hz)
t = 1   # Duration of signal (s)
n = np.arange(0, t, 1/fs)  # Time array

# Square wave generation
duty = 20  # Duty cycle (%) of the square wave
s = np.zeros(len(n))  # Initialize square wave array
for i in range(len(n)):
    if np.floor(2 * fc * n[i]) % 2 == 0:  # Square wave with frequency fc
        s[i] = 1  # Set square wave high

# Generating sine wave
m = np.sin(2 * np.pi * fm * n)  # Sine wave with frequency fm

# PAM waveform generation (Pulse Amplitude Modulation)
period_samp = len(n) / fc  # Period of carrier wave in samples
ind = np.arange(0, len(n), int(period_samp))  # Indices for carrier wave
on_samp = int(np.ceil(period_samp * duty / 100))  # Number of samples for pulse ON duration
pam = np.zeros(len(n))  # Initialize PAM waveform array
for i in ind:
    pam[i:i+on_samp] = m[i]  # Assign modulating signal during pulse ON duration

# Plotting
plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.plot(n, s)
plt.title('Square Wave')
plt.ylim(-0.2, 1.2)  # Set y-axis limits

plt.subplot(3, 1, 2)
plt.plot(n, m)
plt.title('Sine Wave')
plt.ylim(-1.2, 1.2)  # Set y-axis limits

plt.subplot(3, 1, 3)
plt.plot(n, pam)
plt.title('PAM Waveform')
plt.ylim(-1.2, 1.2)  # Set y-axis limits

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()









# Parameters Setup:

# fc: Carrier frequency.
# fm: Modulating frequency.
# fs: Sampling frequency.
# t: Duration of the signal.
# n: Time array from 0 to t with a sampling frequency of fs.
# Square Wave Generation:

# duty: Duty cycle of the square wave.
# s: Array to hold the square wave.
# Loop iterates through each sample and sets the square wave high or low based on the condition.
# Sine Wave Generation:

# m: Array to hold the sine wave generated using NumPy's sin function.
# PAM Waveform Generation:

# period_samp: Period of the carrier wave in samples.
# ind: Indices for the carrier wave.
# on_samp: Number of samples for pulse ON duration.
# pam: Array to hold the PAM waveform.
# Loop assigns the modulating signal during the pulse ON duration.
# Plotting:

# Three subplots are created to visualize the square wave, sine wave, and PAM waveform.
# Y-axis limits are set to ensure proper visualization.
# tight_layout() adjusts subplot parameters to give enough space between subplots.