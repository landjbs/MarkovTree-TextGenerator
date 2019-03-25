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

        if type(wordList) is list:
            self.wordLsit = wordList
        else:
            raise ValueError("Usage: wordList must be type list")

class Node:
    def __init__(self, ):
