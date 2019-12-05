import mido
from mido import Message, MidiFile, MidiTrack
from markov_chain.markov_model import MarkovModel

corpus_file = MidiFile('music/eflat_major/chp_op18.mid', clip=True)
messages = (message for track in corpus_file.tracks for message in track)

# TODO: Make markov model init work with a generator not just a list
mkv = MarkovModel(midi_track=list(messages), order=2)

# Type 0 single track file
gen_midi = MidiFile(type=0)
track = MidiTrack()
gen_midi.tracks.append(track)

for message in mkv.sample(10000):
    # print(message)
    track.append(message)

gen_midi.save('generated.mid')
