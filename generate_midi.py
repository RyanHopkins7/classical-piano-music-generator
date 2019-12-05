import mido
from mido import Message, MidiFile, MidiTrack
from markov_chain.markov_model import MarkovModel
from os import listdir

corpus_files = (MidiFile(f'music/eflat_major/{file_name}', clip=True) for file_name in listdir('music/eflat_major'))

# lol 
messages = (message for f in corpus_files for track in f.tracks[1:3] for message in track)

# TODO: Make markov model init work with a generator not just a list
mkv = MarkovModel(midi_track=list(messages), order=3)

# Type 0 single track file
gen_midi = MidiFile(type=0)
track = MidiTrack()
gen_midi.tracks.append(track)

for message in mkv.sample(10000):
    # print(message)
    track.append(message)

gen_midi.save('generated.mid')
