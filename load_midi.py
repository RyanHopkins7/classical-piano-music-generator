import mido
from mido import MidiFile

# E flat major
mid = MidiFile('music/eflat_major/chp_op18.mid', clip=True)
print(mid)

for track in mid.tracks:
    for msg in track:
        print(msg)
    # print('Track {}: {}'.format(i, track.name))
    # with open('data.txt', 'a') as f:
    #     messages = []
    #     for msg in track:
    #         messages.append(str(msg))
    #     print(messages)
            # f.write(str(msg) + '\n')

