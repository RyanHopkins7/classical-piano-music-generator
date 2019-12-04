import random
from memory import Memory

class MarkovChain:
    def __init__(self, midi_file=None, order=1):
        self.memory = Memory(order=order)

        for i in range(10):
            self.memory.enqueue(i)

        for node in self.memory:
            print(node.data)

    def sample(self):
        pass

    def generate_file(self):
        pass

x = MarkovChain(order=5)
