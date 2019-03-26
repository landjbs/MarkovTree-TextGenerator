class Leaf:
    """
    Word following n previous words
    """
    def __init__(self, name, counter):
        # Name of nth word
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Usage: name must be type string")
        # distance from inital word
        if type(counter) is int:
            self.counter = counter
        else:
            raise ValueError("Usage: counter must be type int")
        # list of words between nth word and initial word
        self.wordList = []

    def add(self, word):
        if type(word) is str:
            self.wordList.append(word)
        else:
            raise ValueError("Usage: added word must be type string")

        word_present = False
        for i,pair in enumerate(self.wordList):
            if pair[0] == self.newWord:
                pair[1] += 1
                word_present = True
        if word_present = false

class Node:
    def __init__(self, ):
