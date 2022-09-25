import librosa
import numpy as np
from mido import MidiFile
import mido
from midiutil.MidiFile import MIDIFile
from random import randrange


# Track data
data = MidiFile('test.mid')
# data = MidiFile('bad1.mid')

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

"""
Example note:
pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)
"""

"""
Create 127 * 127 adjacency matrix
since there are 127 different MIDI note numbers.

For example MIDI note number 28 equals piano key E1 and 41 key F2 etc.
Read more here:
inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
"""
midi_notes_matrix = matrix = np.zeros((127, 127), dtype=int)
starting_note = None

# Insert MIDI changes to the adjacency matrix
for i, track in enumerate(data.tracks):
    # print(f'Track ${i}: ${track.name}')
    note_from = None
    for message in track:
        # print(message)
        if message.type == 'note_on':
            if not starting_note:
                starting_note = message.note
            # note_from is the current note that we are
            # moving from to the next note
            if not note_from:
                note_from = message.note
            midi_notes_matrix[note_from, message.note] += 1
            note_from = message.note

            
current_note = starting_note
next_note = None

notes = [librosa.midi_to_note(current_note)]

for row in range(127):
    for col in range(127):
        if midi_notes_matrix[row, col] > 0:
            next_note = col
            notes.append(librosa.midi_to_note(next_note))
            next_note = col
            pass



# Current beat, start on beat 0
current_beat = 0

# Add notes to the MIDI track
for note in notes:
    mf.addNote(
      track=midi_track,
      channel=channel,
      pitch=librosa.note_to_midi(note),
      time=current_beat,
      duration=randrange(2,4),
      volume=randrange(70, 100)
    )
    current_beat += randrange(0, 4)


# Write it to disk as wave file
with open('output.mid', 'wb') as output:
    mf.writeFile(output)