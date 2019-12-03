class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class Memory:
    """ Memory buffer implemented as a linked list based queue for MarkovChain's higher order functionality """    

    def __init__(self, order=1):
        self.head = None
        self.tail = None

        for i in range(order):
            self.enqueue(i)

    def enqueue(self, data=None):
        if self.head is None:
            self.head = Node(data=data)
            self.tail = self.head
        else:
            new_node = Node(data=data)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """ It is not necessary to return node's value due to implementation """
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:
                self.tail = None

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