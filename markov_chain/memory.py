class Node:
    def __init__(self, state=None, next_node=None, decay=1):
        self.state = state
        self.next = next_node
        # Decay factor calculated using delta time. Will affect likelihood that specific node is used for sampling
        self.decay = decay

class Memory:
    """ Memory buffer implemented as a linked list based queue for MarkovChain's higher order functionality """    

    def __init__(self, order=1):
        self.head = None
        self.tail = None
        self.order = order
        self.length = 0

    def enqueue(self, state=None):
        """ Add a node to the start of the queue with data memory. Length will never exceed order """
        self.length += 1
        if self.length > self.order:
            self.dequeue()

        if self.head is None:
            self.head = Node(state=state)
            self.tail = self.head
        else:
            new_node = Node(state=state)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """ Remove a node from the end of the queue. Returning is not necessary due to implementation """
        if self.head is not None:
            self.length -= 1
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def clear(self):
        """ Clear memory """
        self.head = None
        self.tail = None

    def serialize(self):
        """ Serializes memory queue in the form of a tuple, making it hashable """
        return tuple(node.state for node in self)

    def __len__(self):
        return self.length

    def __iter__(self):
        return MemoryIterator(self.head)

class MemoryIterator:
    """ Make memory queue iterable """

    def __init__(self, head):
        self.current_node = head

    def __next__(self):
        if self.current_node is not None:
            prev_node = self.current_node
            self.current_node = prev_node.next
            return prev_node

        raise StopIteration