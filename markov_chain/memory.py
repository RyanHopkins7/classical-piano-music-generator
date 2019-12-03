class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class Memory:
    """ Memory buffer implemented as a linked list based queue for MarkovChain's higher order functionality """    

    def __init__(self, order=1):
        self.head = Node(data=0)
        prev_node = self.head

        for i in range(order-1):
            prev_node.next = Node(data=i+1)
            prev_node = prev_node.next

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