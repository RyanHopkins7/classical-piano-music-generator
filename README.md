# Classical Piano Music Generator

This application generates piano music in midi form using an nth order Markov model trained off of classical piano music.
A Flask web app is included as a simple interface to generate musical pieces using Markov models of order 1 through 8. 

Composers currently in corpus data: Chopin, Beethoven.

## Getting Started

These instructions will get you a copy of this project up and running on your local machine so you can 
generate your own music and add your own midi files to the training data.

### Prerequisites

This is a Python 3 project and requires the latest version of Python and a virtual environment. 

### Installing

1. Download or clone this repository.

2. Set up your python virtual environment in the cloned directory.

3. Install all required packages from requirements.txt.

### Adding midi files to training_music

1. Add multi-track midi files to training_music/multi_track.

2. Run 'python3 merge_midi_tracks.py merge_dataset' to merge all midi files from training_music/multi_track from multi track midi files to single track midi files and save them in training_music/single_track. It is necessary for midi music to be single track for them to train the Markov model. 

### Running the code

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

