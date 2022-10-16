from Trie import trie
import librosa
from mido import MidiFile
from midiutil.MidiFile import MIDIFile
import numpy as np
from random import randrange
import functools

T = trie.Trie()

def predict_next_note(note):
    """Predict next note based on current state"""
    bigrams_with_current_note = dict((note, appereance) for note, appereance in T.search(note))
    
    if len(bigrams_with_current_note) == 0:
        return None

    appereance = functools.reduce(lambda a, b: a + b, bigrams_with_current_note.values())

    # convert apperance into probabilities
    for bigram in bigrams_with_current_note.keys():
        bigrams_with_current_note[bigram] = bigrams_with_current_note[bigram] / appereance

    # create list of possible options for the next note
    options = [bigram.split('-')[1] for bigram in bigrams_with_current_note.keys()]
    
    # create list of probability distribution
    probabilities = list(bigrams_with_current_note.values())

    # return random prediction
    return np.random.choice(options, p=probabilities)

def generate_sequence(note, n):
    """Generate sequence of n length"""
    sequence = []

    for i in range(n):
        next_note = predict_next_note(note)
        # Break if there is no next note to move from the current one
        if next_note == None:
            break
        else:
            sequence.append(next_note)
            note = sequence[-1]
    return sequence

def write_midi_to_disk(sequence):
    """Create MIDI-file from the generated sequence"""

    # Default bpm to 200 if tempo does not exist in the midi file
    # bpm = mido.tempo2bpm(data.tracks[0][0].tempo) if hasattr(data.tracks[0][0], 'tempo') else 200
    bpm = 200
    channel = 0

    # Create your MIDI object
    mf = MIDIFile(1)  # only 1 track
    midi_track = 0    # the only track

    time = 0 # start at the beginning
    mf.addTrackName(midi_track, time, "Sample Track")
    mf.addTempo(midi_track, time, bpm)

    # Current beat, start on beat 0
    current_beat = 0

    # Add notes to the MIDI track
    for note in sequence:
        mf.addNote(
            track=midi_track,
            channel=channel,
            pitch=librosa.note_to_midi(note),
            time=current_beat,
            duration=randrange(1,4),
            volume=randrange(70, 100)
        )
        current_beat += randrange(1, 3)

    # Write it to disk
    with open('output.mid', 'wb') as output:
        mf.writeFile(output)

def generate_from_midi(data):
    """Generate sequence by using MIDI-file as a training data"""

    starting_note = None
    current_note = None

    # Insert MIDI notes into Trie data structure as bigrams
    for track in data.tracks:
        for message in track:
            if message.type == 'note_on':
                if starting_note == None or current_note == None:
                    starting_note = librosa.midi_to_note(message.note, unicode=False)
                    current_note = librosa.midi_to_note(message.note, unicode=False)
                    pass
                else:
                    next_note = librosa.midi_to_note(message.note, unicode=False)
                    T.insert(f'{current_note}-{next_note}')
                    current_note = next_note
                
    return generate_sequence(starting_note, 30)

def generate_from_user_input():
    """Generate sequence using the user input as a training data"""

    print('\nEnter notes to generate music from, (for example C, D#, E, E#, F, etc...)')
    print('Enter empty input to stop reading input from user. \n')
    
    notes = librosa.midi_to_note(list(range(60, 72)), octave=False, unicode=False)
    sequence = []

    while True:
        note = input('Enter note: ').capitalize()
        if not note:
            break
        elif note not in notes:
            print(f'Invalid input, note must equal one of the following: {notes}')
        elif note in notes:
            sequence.append(note)
            print(f'Added notes: {sequence}')

    starting_note = sequence[0]
    current_note = starting_note

    # Insert MIDI notes into Trie data structure as bigrams
    for note in sequence[1:]:
        next_note = note
        T.insert(f'{current_note}-{next_note}')
        current_note = next_note
                
    return generate_sequence(starting_note, 30)

def main():
    print('Enter number "1" to use a MIDI-file as a training data: ')
    print('Enter number "2" to insert notes manually from console:')
    option = input('Choose option: ')
    
    if option == '1':
        file_name = input('Enter the name of the MIDI-file: ')
        data = MidiFile(file_name)
        generated_sequence = generate_from_midi(data)
        print(f'Generated sequence = {generated_sequence}')
        write_midi_to_disk(generated_sequence)
    elif option == '2':
        generated_sequence = generate_from_user_input()
        print(f'Generated sequence = {generated_sequence}')
        write_midi_to_disk(generated_sequence)
    else:
        quit()

main()