from mido import MidiFile
from index import *
import librosa

def test_generated_output_midi_equals_generated_sequences():
    data = MidiFile('bad.mid')

    lenght_of_sequence = 50
    generated_sequences = generate_from_midi(data, lenght_of_sequence)
    write_midi_to_disk(generated_sequences)

    generated_data = MidiFile('output.mid')
    channels = { str(channel) : [] for channel in range(0, 16) }
    
    for track in generated_data.tracks:
        for message in track:
            if message.type == 'note_on':
                channels[str(message.channel)].append(librosa.midi_to_note(message.note))

    # Check that the lengths are the same on every channel
    for channel, sequence in generated_sequences:
        assert len(sequence) == len(channels[channel])

    # Check that the sequences are the same on every channel
    for channel, sequence in generated_sequences:
        assert sequence == channels[channel]

    for channel, sequence in generated_sequences:
        assert sequence != channels[channel].append('C4')
    