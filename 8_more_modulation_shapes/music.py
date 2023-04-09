import rtmidi
import time
import sys
from rtmidi.midiconstants import CONTROL_CHANGE
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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
    scaled_value = out_min = (scaled_value * r_span)
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


def modulation_shape(shape: str, speed_of_wave: float, max_duration: float):
    """ Function that shows modulation shape """
    # Create a list of values from 0 to the max_duration value with an interval of 0.1
    x = np.arange(0, max_duration, 0.01)

    if shape == "sine":
        y = np.sin(2 * np.pi / speed_of_wave * x)
    elif shape == "saw":
        y = signal.sawtooth(2 * np.pi / speed_of_wave * x)
    elif shape == "square":
        y = signal.square(2 * np.pi / speed_of_wave * x)
    else:
        print("Not valid wave")
        sys.exit()
    plt.plot(x, y)
    plt.ylabel(f"Amplitude = {shape} (time)")
    plt.xlabel("Time")
    plt.title("Modulation shape")
    plt.axhline(y=0, color="black")
    plt.show()




modulation_shape("sine", 1.0, 2)