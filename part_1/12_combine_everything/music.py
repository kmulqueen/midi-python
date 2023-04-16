import threading
import rtmidi
import time
from rtmidi.midiconstants import CONTROL_CHANGE
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from midi.part_1.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)

cc_num = 1
channel = 2
BPM = 60


def convert_range(value, in_min, in_max, out_min, out_max):
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)


def play_melody(melody, bpm):
    """ Function that plays melody in time"""
    for pitch, duration in melody:
        note_on = [CHANNEL_1, pitch, 112]
        note_off = [CHANNEL_2, pitch, 0]
        dur = duration_to_time_delay(duration, bpm)
        midi_out.send_message(note_on)
        time.sleep(dur)
        midi_out.send_message(note_off)


def play_modulation(y, max_duration):
    """ Function that sends a modulation shape"""
    pause_duration = max_duration / y.size
    for val in y:
        val = convert_range(val, -1.0, 1.0, 0, 127)
        mod = ([CONTROL_CHANGE | channel, cc_num, val])
        midi_out.send_message(mod)
        time.sleep(pause_duration)


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
        raise ValueError(f"Unknown shape: {shape}")
    plt.plot(x, y)
    plt.ylabel(f"Amplitude = {shape} (time)")
    plt.xlabel("Time")
    plt.title("Modulation shape")
    plt.axhline(y=0, color="black")
    plt.show()
    return y


def duration_of_melody(melody, bpm):
    return sum(duration_to_time_delay(duration, bpm) for _, duration in melody)


def duration_to_time_delay(duration, bpm):
    if duration == "w":
        factor = 4
    elif duration == "h":
        factor = 2
    elif duration == "q":
        factor = 1
    elif duration == "e":
        factor = 0.5
    elif duration == "s":
        factor = 0.25
    else:
        assert False

    bps = bpm / 60
    return factor * bps


def main():
    melody = [(60, "e"), (67, "q"), (62, "q"), (67, "e"), (60, "q")]
    dur = duration_of_melody(melody, BPM)
    modulation = modulation_shape("sine", 1, dur)
    t1 = threading.Thread(target=play_melody, args=(melody, BPM))
    t2 = threading.Thread(target=play_modulation, args=(modulation, dur))

    t1.start()
    t2.start()


main()
