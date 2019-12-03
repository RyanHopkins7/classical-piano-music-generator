import random
from memory import Memory

class MarkovChain:
    def __init__(self, midi_file=None, order=10):
        self.memory = Memory(order=order)
        for node in self.memory:
            print(node.data)

    def sample(self):
        pass

    def generate_file(self):
        pass

x = MarkovChain()
