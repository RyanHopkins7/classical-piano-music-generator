import mido
from mido import MidiFile

# E flat major
mid = MidiFile('music/chp_op18.mid', clip=True)
print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

