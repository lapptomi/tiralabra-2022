from mido import MidiFile
from index import generate_from_midi

def test_generated_sequence_lengths():
    data = MidiFile('bad.mid')
    lenght_of_sequence_1 = 30
    lenght_of_sequence_2 = 50
    
    for channel, sequence in generate_from_midi(data, lenght_of_sequence_1):
        assert len(sequence) == lenght_of_sequence_1

    for channel, sequence in generate_from_midi(data, lenght_of_sequence_2):
        assert len(sequence) == lenght_of_sequence_2

    # Test another MIDI-file
    data2 = MidiFile('bb-king.mid')
    for channel, sequence in generate_from_midi(data2, lenght_of_sequence_1):
        assert len(sequence) == lenght_of_sequence_1

    for channel, sequence in generate_from_midi(data2, lenght_of_sequence_2):
        assert len(sequence) == lenght_of_sequence_2
