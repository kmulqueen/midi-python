import rtmidi
import time
import random
from note_dictionary import create_midi_notes_dict
from create_scale_dictionary import get_scale_notes

midi_out = rtmidi.MidiOut()

# List of available MIDI ports
ports = midi_out.get_ports()

# Open port
port = 4  # loopMIDI Port 4
midi_out.open_port(port)

# Note information
pitch = 60
scale = "major"
num_octaves = 1
tempo = 0.2

# Create a note_dictionary from start of middle c up 12 semitones
note_dictionary = create_midi_notes_dict(pitch, pitch + 12)
note_list = list(note_dictionary.keys())

# Create a list of notes found in scale
scale_notes = get_scale_notes(pitch, scale, num_octaves)

with midi_out:
    # Play minor scale from middle C
    for idx in range(num_octaves * len(scale_notes)):
        note = scale_notes[idx % len(scale_notes)] + (idx // len(scale_notes)) * 12
        print(idx, " - ", note)
        channel_1 = 0x90
        channel_2 = 0X80
        velocity = 50
        note_on = [channel_1, note, velocity]
        note_off = [channel_2, note, 0]
        midi_out.send_message(note_on)
        time.sleep(tempo)
        midi_out.send_message(note_off)

    # Play random notes from note_dictionary
    # for idx, note in enumerate(scale_notes):
    #     start = scale_notes[0]
    #     end = scale_notes[-1]
    #     random_note = random.randrange(start, scale_notes[-1])
    #     print(idx, note, start, end, random_note)
    #     channel_1 = 0x90
    #     channel_2 = 0X80
    #     velocity = 50
    #     note_on = [channel_1, random_note, velocity]
    #     note_off = [channel_2, random_note, 0]
    #     midi_out.send_message(note_on)
    #     time.sleep(tempo)
    #     midi_out.send_message(note_off)