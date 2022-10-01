from Trie import trie
import librosa
from mido import MidiFile
import mido
from midiutil.MidiFile import MIDIFile
import numpy as np
from random import randrange

T = trie.Trie()

# Track data
data = MidiFile('test.mid')

# Default bpm to 200 if tempo does not exist in the midi file
bpm = mido.tempo2bpm(data.tracks[0][0].tempo) if hasattr(data.tracks[0][0], 'tempo') else 200
channel = 0
volume = 100


# Create your MIDI object
mf = MIDIFile(1)     # only 1 track
midi_track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(midi_track, time, "Sample Track")
mf.addTempo(midi_track, time, bpm)

starting_note = librosa.midi_to_note(data.tracks[1][1].note)
current_note = starting_note

# Insert MIDI notes into Trie data structure
for track in data.tracks:
    for message in track:
        if message.type == 'note_on':
            next_note = librosa.midi_to_note(message.note)
            T.insert(current_note+'-'+next_note)
            current_note = next_note

def predict_next_note(note):
    """Predict next note based on current state"""
    count_appearance = dict((note, appereance) for note, appereance in T.search(note))

    # convert apperance into probabilities
    for key in count_appearance.keys():
        count_appearance[key] = count_appearance[key]/len(T.search(note))

    # create list of possible options for the next chord
    options = [key.split('-')[1] for key in count_appearance.keys()]
    
    # create  list of probability distribution
    probabilities = list(count_appearance.values())

    # return random prediction
    return np.random.choice(options, p=probabilities)


def generate_sequence(note, n):
    """Generate sequence of n length"""
    notes = []
    for i in range(n):
        notes.append(predict_next_note(note))
        note = notes[-1]
    return notes

# n equals the length of the sequence
n = 30
sequence = generate_sequence(starting_note, n)
print(f'Generated sequence = {sequence}')

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