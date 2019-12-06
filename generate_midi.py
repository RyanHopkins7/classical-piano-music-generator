import mido
from mido import Message, MidiFile, MidiTrack
from markov_chain.markov_model import MarkovModel
from os import listdir

def generate_midi(mkv_order=1, num_messages=10000):
    """
    Generates and saves a midi file using an Nth order markov chain trained on midi files from music/single_track.
    Generated midi file is saved in music/generated.mid.
    Args:
        mkv_order (int): The order of the markov chain that should be used to generate the file
        num_messages (int): The number of mido messages to be added to the generated midi file 
    """
    corpus_files = (MidiFile(f'music/single_track/{file_name}', clip=True) for file_name in listdir('music/single_track'))

    messages = (message for f in corpus_files for message in f.tracks[0])

    # TODO: Make markov model init work with a generator not just a list
    mkv = MarkovModel(midi_track=list(messages), order=mkv_order)

    # Type 0 single track file
    gen_midi = MidiFile(type=0)
    track = MidiTrack()
    gen_midi.tracks.append(track)

    for message in mkv.sample(num_messages):
        track.append(message)

    gen_midi.save('static/generated.mid')

if __name__ == "__main__":
    generate_midi(mkv_order=4)
