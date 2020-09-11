#!/usr/bin/python3
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read('secretaudio.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.gca().invert_yaxis()
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()