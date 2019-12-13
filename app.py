from flask import Flask, render_template, request, Response, send_file
from generate_midi import generate_midi

app = Flask(__name__)

"""
Note: If more than one person is expected to use this site at a time, sessions will need to be implemented
to prevent specific users' generated files from overwriting other users' generated files
"""

# TODO: save markov models of orders 1 - 8 and load at start of app to improve speed

@app.route('/')
def index():
    ''' Display home page '''
    return render_template('index.html')

@app.route('/generate-midi', methods=['POST'])
def generate_midi_route():
    ''' Generate a new midi file '''
    order = int(request.form['order'])
    generate_midi(mkv_order=order)
    return Response("Finished generating new MIDI file")

@app.route('/serve-midi')
def serve_midi():
    ''' Serve most recently generated midi file '''
    return send_file('generated.mid')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)