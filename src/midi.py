from Trie import trie
import librosa
from mido import MidiFile
import mido
from midiutil.MidiFile import MIDIFile

T = trie.Trie()

# This does not work yet correctly
def nGrams(sequence, n):
    notes = sequence.split('-')
    total = len(notes) - n;
    grams = [];

    for i in range(total):
        seq = ''
        for j in range(i):
            seq += notes[j] + ' '

        grams.append(seq)
    return grams


# Track data
data = MidiFile('test.mid')
#data = MidiFile('bad1.mid')

# Default bpm to 150 if tempo does not exist in the midi file
bpm = mido.tempo2bpm(data.tracks[0][0].tempo) if hasattr(data.tracks[0][0], 'tempo') else 150
channel = 0
volume = 100

# Create your MIDI object
mf = MIDIFile(1)     # only 1 track
midi_track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(midi_track, time, "Sample Track")
mf.addTempo(midi_track, time, bpm)

seq = ''

# Insert MIDI notes into the Trie data structure
for i, track in enumerate(data.tracks):
    for message in track:
        # print(message)
        if message.type == 'note_on':
            print(message.note)
            # print(librosa.midi_to_note(message.note))
            T.insert(librosa.midi_to_note(message.note))
            seq += librosa.midi_to_note(message.note)+'-'

            
print(T.search(''))