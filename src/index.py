from datetime import datetime
from Trie import trie
import librosa
from mido import MidiFile
from midiutil.MidiFile import MIDIFile
import numpy as np
from random import randrange
import functools

T = trie.Trie()

def predict_next_note(note, channel):
    """Predict next note based on current state"""

    bigrams_with_current_note = dict((bigram, appereance) for bigram, appereance in T.search(note))
    bigrams_with_current_channel = {
        bigram.split('/')[0] : count 
            for bigram, count in bigrams_with_current_note.items() if bigram.split('/')[1] == channel
    }

    if len(bigrams_with_current_channel) == 0:
        return None

    appereance = functools.reduce(lambda a, b: a + b, bigrams_with_current_channel.values())

    # Convert apperance into probabilities
    for bigram in bigrams_with_current_channel.keys():
        bigrams_with_current_channel[bigram] = bigrams_with_current_channel[bigram] / appereance

    # Create list of possible options for the next note
    options = [bigram.split('-')[1] for bigram in bigrams_with_current_channel.keys()]
    
    # Create list of probability distribution
    probabilities = list(bigrams_with_current_channel.values())

    # Return random prediction
    return np.random.choice(options, p=probabilities)

def generate_sequence(note, channel, n):
    """Generate sequence of n length"""
    sequence = []

    for i in range(n):
        next_note = predict_next_note(note, channel)
        if next_note == None:
            # Break if there is no next note to move from the current one
            break
        else:
            sequence.append(next_note)
            note = sequence[-1]
    return sequence

def generate_from_midi(data, length):
    """Generate sequence by using MIDI-file as a training data"""

    starting_notes = []
    added_channels = []

    # channels = { '0': [], '1': [], ...,  '15': [] }
    channels = { str(channel) : [] for channel in range(0, 16) }

    # Insert notes to the dictionary by channel
    for track in data.tracks:
        for message in track:
            if message.type == 'note_on':
                if message.channel not in added_channels:
                    # Add the starting notes for every channel
                    starting_notes.append(f'{librosa.midi_to_note(message.note)}/{message.channel}')
                    added_channels.append(message.channel)
                channels[str(message.channel)].append(librosa.midi_to_note(message.note))

    # Insert the notes into Trie as bigrams
    for channel, seq in channels.items():
        if len(seq) < 2:
            # Pass if there is less than two notes in the sequence
            pass
        for index in range(1, len(seq)-1):
            T.insert(f'{seq[index-1]}-{seq[index]}/{channel}')
    
    generated_sequences = []
    # Generate sequences for every channel
    for obj in starting_notes:
        note, channel = obj.split('/')
        generated_sequences.append((channel, generate_sequence(note, channel, length)))

    return generated_sequences

def write_midi_to_disk(sequences):
    """Create MIDI-file from the generated sequence"""

    # Create your MIDI object
    bpm = 200
    midi_file = MIDIFile(15)
    midi_track = 0

    time = 0 # Start at the beginning
    midi_file.addTrackName(midi_track, time, "Sample Track")
    midi_file.addTempo(midi_track, time, bpm)

    # Current beat, start on beat 0
    current_beat = 0

    # Add notes to the MIDI tracks
    for channel, sequence in sorted(sequences):
        for note in sequence:
            midi_file.addNote(
                track=int(channel),
                channel=int(channel),
                pitch=librosa.note_to_midi(note),
                time=current_beat,
                duration=randrange(1,4),
                volume=randrange(50, 100)
            )
            current_beat += randrange(1, 8)
        current_beat = 0
    
    # Write it to disk
    with open('output.mid', 'wb') as output:
        midi_file.writeFile(output)

    print('\nMIDI-file "output.mid" generated successfully!')

def main():
    file_name = input('\nEnter the name of the MIDI-file to use as a training data: ')
    data = MidiFile(file_name)
    length_of_sequence = int(input('Enter the length of the sequence to generate, for example 30: '))

    start_time = datetime.now()
    generated_sequence = generate_from_midi(data, length_of_sequence)
    write_midi_to_disk(generated_sequence)
    end_time = datetime.now()

    print(f'Duration (hour:minute:second.ms): {end_time - start_time}')

if __name__ == "__main__":
    main()
