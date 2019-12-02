import mido
from mido import MidiFile

# E flat major
mid = MidiFile('music/eflat_major/chp_op18.mid', clip=True)
print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    with open('data.txt', 'a') as f:
        for msg in track:
            f.write(str(msg) + '\n')

