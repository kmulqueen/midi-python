import rtmidi
import time
from midi.constants import *
midi_out = rtmidi.MidiOut()
midi_out.open_port(PORT)


def send_notes(pitch=60, repeat=1):
    for note in range(repeat):
        note_on = [CHANNEL_1, pitch, 50]
        note_off = [CHANNEL_2, pitch, 0]
        midi_out.send_message(note_on)
        time.sleep(0.4)
        midi_out.send_message(note_off)


with midi_out:
    pitch = 60
    for i in range(len(SCALES["major"])):
        send_notes(pitch + SCALES["major"][i])


