from flask import Flask, render_template, request, Response, send_file
from model.markov_model import MarkovModel
from mido import Message, MidiFile, MidiTrack
from os import listdir

app = Flask(__name__)

corpus_files = (MidiFile(f'training_music/single_track/{file_name}', clip=True) for file_name in listdir('training_music/single_track'))

messages = [message for f in corpus_files for message in ['START'] + f.tracks[0] + ['END']]

mkv_models = [
    MarkovModel(midi_data=messages, order=1),
    MarkovModel(midi_data=messages, order=2),
    MarkovModel(midi_data=messages, order=3),
    MarkovModel(midi_data=messages, order=4),
    MarkovModel(midi_data=messages, order=5),
    MarkovModel(midi_data=messages, order=6)
]

@app.route('/')
def index():
    ''' Display home page '''
    return render_template('index.html')

@app.route('/generate-midi', methods=['POST'])
def generate_midi_route():
    ''' Generate a new midi file '''
    mkv_order = int(request.form['order'])

    mkv = mkv_models[mkv_order-1]

    # Type 0 single track file
    gen_midi = MidiFile(type=0)
    track = MidiTrack()
    gen_midi.tracks.append(track)

    for message in mkv.sample():
        track.append(message)

    gen_midi.save(f'generated/generated{mkv_order}.mid')

    return Response("Finished generating new MIDI file")

@app.route('/serve-midi')
def serve_midi():
    ''' Serve most recently generated midi file of given order '''
    mkv_order = request.args['order']
    return send_file(f'generated/generated{mkv_order}.mid')

if __name__ == '__main__':
    app.run()