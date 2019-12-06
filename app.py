from flask import Flask, render_template, request, Response
from generate_midi import generate_midi

app = Flask(__name__)

"""
Note: If more than one person is expected to use this site at a time, sessions will need to be implemented
to prevent specific users' generated files from overwriting other users' generated files
"""

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

if __name__ == '__main__':
    app.run(debug=True)