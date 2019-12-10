import mido
from mido import Message, MidiFile, MidiTrack
from model.markov_model import MarkovModel
from os import listdir
import sys

def generate_midi(mkv_order=4):
    """
    Generates and saves a midi file using an Nth order markov chain trained on midi files from training_music/single_track.
    Generated midi file is saved in static/generated.mid.
    Args:
        mkv_order (int): The order of the markov chain that should be used to generate the file
        num_messages (int): The number of mido messages to be added to the generated midi file 
    """
    corpus_files = (MidiFile(f'training_music/single_track/{file_name}', clip=True) for file_name in listdir('training_music/single_track'))

    messages = (message for f in corpus_files for message in ['START'] + f.tracks[0] + ['END'])

    mkv = MarkovModel(midi_track=messages, order=mkv_order) 

    # Type 0 single track file
    gen_midi = MidiFile(type=0)
    track = MidiTrack()
    gen_midi.tracks.append(track)

    for message in mkv.sample():
        track.append(message)

    """
    ISSUE: generated midi files get cached by javascript web audio and don't update
    """

    gen_midi.save('static/generated.mid')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        order = int(sys.argv[1])
    else:
        order = 4
    generate_midi(mkv_order=order)
