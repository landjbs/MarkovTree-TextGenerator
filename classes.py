from helpers import str_check

class Leaf:
    """
    The Leaf stems from a sequence of n words, and tracks the frequency
    at which different words follow. The Leaf provides the selection from which
    a next word will be chosen
    """
    def __init__(self, name, counter):
        """
        Initialize leaf with word and counter of distance from base word
        """
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
        """
        Adds single word to wordList of Leaf
        """
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
    """

    """
    def __init__(self, seqList, endWord):
        self.leafNode = False
        # name of first word
        self.name = seqList[0]
        # if not nth node
        if len(seqList) > 1:
            # create next layer
            self.center = Node(seqList[1:], endWord)
        else:
            # create leaf at end of nth node
            self.leafNode = True
            self.center = Leaf(self.name, 1)
            self.center.add(endWord)
        # set room for horizontal nodes
        self.left = None
        self.right = None

    def search_add(self, seqList, endWord):

        check_word = seqList[0]
        condition = str_check(check_word, self.name)
        # go one layer further
        if condition == 0:
            if self.leafNode:
                self.center.add(endWord)
            else:
                self.center.search_add(seqList[1:], endWord)
        # horizontal movement - word can be found later alphabetically
        elif condition == -1:
            if self.left is None:
                self.left = Node(seqList, endWord)
            else:
                self.left.search_add(seqList, endWord)
        # horizontal movement - word can be found earlier alphabetically
        else:
            if self.right is None:
                self.right = Node(seqList, endWord)
            else:
                self.right.search_add(seqList, endWord)
