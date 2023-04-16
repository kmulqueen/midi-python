from note_dictionary import create_midi_notes_dict
import json

midi_notes = create_midi_notes_dict()

with open('scales.json') as scales_file:
    parsed_json = json.load(scales_file)


def get_scale_notes(pitch, scale_name, octave=1):
    if isinstance(pitch, str):
        pitch = pitch.lower()  # convert pitch to lowercase
        pitch = midi_notes.get(pitch.lower())
    root_note = pitch % 12
    scale = parsed_json[scale_name]
    midi_notes_in_scale = []
    for i in range(octave + 1):
        midi_notes_in_scale += [(note + pitch + (i * 12)) for note in scale]
    return midi_notes_in_scale[:octave * len(scale) + 1]






