from random import choice
try:
    from markov_chain.memory import Memory, Node
except ModuleNotFoundError:
    from memory import Memory, Node

class MarkovModel(dict):
    """ Dictionary based nth order markov model """

    def __init__(self, midi_track=[], order=1):
        self.memory = Memory(order)

        for message in midi_track:
            if isinstance(message, str) and message == 'START':
                self.memory.clear()
                self.memory.enqueue('START')
            else:
                self.add_state(message)

        self.memory.clear()
        self.memory.enqueue('START')

    def add_state(self, new_state):
        """ Add a state to markov model and add new state to memory """
        current_state = self.memory.serialize()
        
        if current_state in self:
            self[current_state].append(new_state)
        else:
            self[current_state] = [new_state]

        self.memory.enqueue(new_state)

    def sample(self):
        """ Return generator from sampling from markov model until an end state is reached """
        starting_state = ('START',)
        while True:
            next_state = choice(self[starting_state])
            self.memory.enqueue(next_state)
            # Continue yielding until an end state is reached
            if not isinstance(next_state, str):
                yield next_state
            else:
                break
            starting_state = self.memory.serialize()
        self.memory.clear()
        self.memory.enqueue('START')

