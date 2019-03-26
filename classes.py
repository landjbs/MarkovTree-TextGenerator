class Leaf:
    """
    The Leaf stems from a sequence of n words, and tracks the frequency
    at which different words follow. The Leaf provides the selection from which
    a next word will be chosen
    """
    def __init__(self, name, counter):
        # Name of nth word
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Usage: name must be type string")
        # number of times leaf is reached in text
        if type(counter) is int:
            self.counter = counter
        else:
            raise ValueError("Usage: counter must be type int")
        # list of all final words that occur, with frequency at which they occur
        self.wordList = []

    def add(self, word):
        # adds a word to the list
        if type(word) is str:
            self.wordList.append(word)
        else:
            raise ValueError("Usage: added word must be type string")
        # search for word in list, add a tally to counter
        word_present = False
        for i, pair in enumerate(self.wordList):
            if pair[0] == self.newWord:
                pair[1] += 1
                word_present = True
        # if word is not in list, add with one tally
        if word_present == False:
            self.wordList.append((self.newWord,1))

        # add tally to the overall leaf counter (denominator for probability)
        self.counter += 1

class Node:
    def __init__(self, seqList, endWord):
        #name of first word
        self.name = seqList[-1]
        #if not nth node
        if len(seqList > 1):
            #create next layer
            self.center = Node(seqList[:-1], endWord)
        else:
            #create leaf at end of nth node
            self.center = Leaf(endWord, 1)
        #set room for horizontal nodes
        self.left = None
        self.right = None
