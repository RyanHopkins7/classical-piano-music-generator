from random import choice
try:
    from markov_chain.memory import Memory, Node
except ModuleNotFoundError:
    from memory import Memory, Node

class MarkovModel(dict):
    """ Dictionary based nth order markov model """

    def __init__(self, midi_track=[], order=1):
        # init_memory used for initializing markov model and adding states
        self.init_memory = Memory(order)
        # memory used for sampling from markov model
        self.memory = Memory(order)

        # Adding states spliced before order allows model to loop to beginning once the end is reached when sampling
        for message in midi_track + midi_track[:order]:
            self.add_state(message)

    def add_state(self, new_state):
        """ Add a state to markov model and add new state to init_memory """
        current_state = self.init_memory.serialize()
        
        if current_state in self:
            self[current_state].append(new_state)
        else:
            self[current_state] = [new_state]

        self.init_memory.enqueue(new_state)

    def sample(self, starting_state=('START',)):
        """ Return generator from sampling from markov model until an end state is reached """
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

