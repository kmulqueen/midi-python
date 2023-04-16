import rtmidi
import numpy as np
import matplotlib.pyplot as plt

from midi.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)

# Value you want to convert, input values, output values
def convert_range(value, in_min, in_max, out_min, out_max):
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)


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
    return amplitude



# sine_waves()
amp = sine_waves_short()

converted_amplitude = []
for number in amp:
    result = convert_range(number, -1, 1, 0, 127)
    converted_amplitude.append(result)
print(converted_amplitude)