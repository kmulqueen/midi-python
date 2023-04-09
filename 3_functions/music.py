import rtmidi
import time
from rtmidi.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)


def send_notes(pitch=60, repeat=1):
    for note in range(repeat):
        print(pitch)
        note_on = [CHANNEL_1, pitch, 50]
        note_off = [CHANNEL_2, pitch, 0]
        midi_out.send_message(note_on)
        time.sleep(0.4)
        midi_out.send_message(note_off)


with midi_out:
    pitch = 60
    for i in range(4):
        send_notes(pitch + i)


