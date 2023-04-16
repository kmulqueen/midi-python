import rtmidi
import numpy as np
import matplotlib.pyplot as plt

from midi.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)


def sine_waves(repeat=1):
    """ Function that shows a lot of sine waves modulation shapes """
    t = np.arange(0, 80, 0.1)  # Time
    amplitude = np.sin(t)  # Height of wave at certain point
    print(t)
    print('amplitude', amplitude)
    plt.plot(t, amplitude)  # Draw
    plt.title("Modulation Shape")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()  # Show

def sine_waves_short(repeat=1):
    """ Function that shows 1 sine wave modulation shape """
    t = np.arange(0, 80, 0.1)  # Time
    amplitude = np.sin(t)  # Height of wave at certain point

    # Use list slicing to get smaller range of elements from time & amplitude
    # The smaller the range the more zoomed in the image is
    plt.plot(t[1:60], amplitude[1:60])  # Draw
    plt.title("Modulation Shape")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True, which="both")
    plt.axhline(y=0)
    plt.show()  # Show

# sine_waves()
sine_waves_short()
