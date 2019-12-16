from flask import Flask, render_template, request, Response, send_file
from generate_midi import generate_midi

app = Flask(__name__)

@app.route('/')
def index():
    ''' Display home page '''
    return render_template('index.html')

@app.route('/generate-midi', methods=['POST'])
def generate_midi_route():
    ''' Generate a new midi file '''
    mkv_order = int(request.form['order'])

    generate_midi(mkv_order=mkv_order)

    return Response("Finished generating new MIDI file")

@app.route('/serve-midi')
def serve_midi():
    ''' Serve most recently generated midi file of given order '''
    mkv_order = request.args['order']
    return send_file(f'generated/generated{mkv_order}.mid')

if __name__ == '__main__':
    app.run()