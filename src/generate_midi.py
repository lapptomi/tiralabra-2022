from random import randrange
from midiutil.MidiFile import MIDIFile

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, 'Sample Track')
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 52           # C4 (middle C)
time = 8             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)


pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 69           # A4
time = 6             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)


# Add some random notes
for i in range(6, 10):
    print(i)
    mf.addNote(
      track=track,
      channel=channel,
      pitch=randrange(30, 80),
      time=randrange(i, i+4),
      duration=randrange(1, 4),
      volume=volume
    )


# Write it to disk
with open('output.mid', 'wb') as output:
    mf.writeFile(output)