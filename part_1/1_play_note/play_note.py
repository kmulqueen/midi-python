import rtmidi
import time

midi_out = rtmidi.MidiOut()

# List of available MIDI ports
ports = midi_out.get_ports()
print("available midi ports: ", ports)

# Open port
port = 4  # loopMIDI Port 4
midi_out.open_port(port)

with midi_out:
    channel_1 = 0x90
    channel_2 = 0X80
    middle_c = 60
    velocity = 50
    note_on = [channel_1, middle_c, velocity]
    note_off = [channel_2, middle_c, 0]
    midi_out.send_message(note_on)
    time.sleep(1)
    midi_out.send_message(note_off)