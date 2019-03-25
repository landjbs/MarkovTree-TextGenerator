class Leaf:
    """
    Word following n previous words
    """
    def __init__(self, name, counter):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Usage: name must be type string")

        if type(counter) is int:
            self.counter = counter
        else:
            raise ValueError("Usage: counter must be type int")

        self.wordList = []

class Node:
    def __init__(self, ):
