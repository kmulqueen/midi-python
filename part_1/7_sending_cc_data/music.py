import rtmidi
import time
from rtmidi.midiconstants import CONTROL_CHANGE
import numpy as np
import matplotlib.pyplot as plt

from midi.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)

cc_num = 75
speed = 0.05
channel = 0

# Value you want to convert, input values, output values
def convert_range(value, in_min, in_max, out_min, out_max):
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)


def send_mod(amplitude, repeat):
    """ Function that sends CC data to MIDI driver"""
    converted_amplitude = []
    for number in amplitude:
        result = convert_range(number, -1, 1, 0, 127)
        converted_amplitude.append(result)
    for _ in range(repeat):
        for value in converted_amplitude:
            mod = ([CONTROL_CHANGE | channel, cc_num, value])
            midi_out.send_message(mod)
            time.sleep(speed)


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
    send_mod(amplitude, repeat)



# sine_waves()
amp = sine_waves_short()