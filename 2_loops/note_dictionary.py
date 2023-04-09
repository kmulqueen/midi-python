def create_midi_notes_dict(start_note=0, end_note=127):
    """
    Creates a dictionary of MIDI note numbers and their corresponding note names.

    Args:
        start_note (int): The MIDI note number to start the dictionary from (default is 0).
        end_note (int): The MIDI note number to end the dictionary at (default is 127).

    Returns:
        dict: A dictionary of MIDI note numbers and their corresponding note names.
    """
    midi_notes = {}
    for note_num in range(start_note, end_note+1):
        octave = note_num // 12 - 1
        note_name = ''
        if note_num % 12 == 0:
            note_name = 'C'
        elif note_num % 12 == 1:
            note_name = 'C#'
        elif note_num % 12 == 2:
            note_name = 'D'
        elif note_num % 12 == 3:
            note_name = 'D#'
        elif note_num % 12 == 4:
            note_name = 'E'
        elif note_num % 12 == 5:
            note_name = 'F'
        elif note_num % 12 == 6:
            note_name = 'F#'
        elif note_num % 12 == 7:
            note_name = 'G'
        elif note_num % 12 == 8:
            note_name = 'G#'
        elif note_num % 12 == 9:
            note_name = 'A'
        elif note_num % 12 == 10:
            note_name = 'A#'
        elif note_num % 12 == 11:
            note_name = 'B'
        note_name += str(octave)
        midi_notes[note_num] = note_name
    return midi_notes
