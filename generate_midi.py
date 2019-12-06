import mido
from mido import Message, MidiFile, MidiTrack
from markov_chain.markov_model import MarkovModel
from os import listdir

def generate_midi(mkv_order=4):
    """
    Generates and saves a midi file using an Nth order markov chain trained on midi files from music/single_track.
    Generated midi file is saved in music/generated.mid.
    Args:
        mkv_order (int): The order of the markov chain that should be used to generate the file
        num_messages (int): The number of mido messages to be added to the generated midi file 
    """
    corpus_files = (MidiFile(f'music/single_track/{file_name}', clip=True) for file_name in listdir('music/single_track'))

    messages = (message for f in corpus_files for message in ['START'] + f.tracks[0] + ['END'])

    mkv = MarkovModel(midi_track=messages, order=mkv_order)

    # Type 0 single track file
    gen_midi = MidiFile(type=0)
    track = MidiTrack()
    gen_midi.tracks.append(track)

    for message in mkv.sample():
        track.append(message)

    """
    TODO: use a global counter and add it to the file name for each newly generated file.
    After X files are generated, delete the last one to prevent too much space from being taken up.
    This should avoid the need for sessions and also get rid of the caching issue.
    """

    gen_midi.save('static/generated.mid')

if __name__ == "__main__":
    generate_midi(mkv_order=4)
