from helpers import str_check
from random import random

class Leaf:
    """
    The Leaf stems from a sequence of n words, and tracks the frequency
    at which different words follow. The Leaf provides the selection from which
    a next word will be chosen
    """
    def __init__(self, name):
        """ Initialize leaf with word and counter of distance from base word """
        assert (isinstance(name, str)), "Usage: name must be type string"
        self.name = name # name of nth word
        self.counter = 0 # number of times leaf is reached in text
        self.wordList = [] # list of all final words with frequency of occurence

    def add(self, word):
        """ Adds single word to wordList of Leaf """
        assert (isinstance(word, str)), "Usage: added word must be type string"
        self.newWord = word
        # search for word in list, add a tally to counter
        word_present = False
        for i, pair in enumerate(self.wordList):
            if pair[0] == self.newWord:
                pair[1] += 1
                word_present = True
        # if word is not in list, add with one tally
        if word_present == False:
            self.wordList.append([self.newWord,1])
        # add tally to the overall leaf counter (denominator for probability)
        self.counter += 1

    def get_word(self):
        print(self.counter, self.wordList)
        num = random() * self.counter
        print(num)
        for i, pair in enumerate(self.wordList):
            num += - pair[1]
            if num <= 0:
                return pair[0]

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
            # print(f"seqList: {seqList} at {self.name}")
            # print("not a leafnode, new node created")
            self.center = Node(seqList[1:], endWord)
        else:
            # create leaf at end of nth node
            # print("leafNode found")
            self.leafNode = True
            self.center = Leaf(self.name)
            self.center.add(endWord)
        # set room for horizontal nodes
        self.left = None
        self.right = None

    def search_add(self, seqList, endWord):

        # print(f"seqList: {seqList} at {self.name}")
        check_word = seqList[0]
        condition = str_check(check_word, self.name)
        # go one layer further
        if condition == 0:
            # print("found word")
            if self.leafNode:
                self.center.add(endWord)
            else:
                self.center.search_add(seqList[1:], endWord)
        # horizontal movement - word can be found later alphabetically
        elif condition == -1:
            if self.left is None:
                # print("left node created")
                self.left = Node(seqList, endWord)
            else:
                self.left.search_add(seqList, endWord)
        # horizontal movement - word can be found earlier alphabetically
        else:
            if self.right is None:
                # print("right node created")
                self.right = Node(seqList, endWord)
            else:
                self.right.search_add(seqList, endWord)

    def nav(self, seqList):
        check_word = seqList[0]
        condition = str_check(check_word, self.name)
        # go one layer further
        if condition == 0:
            # print("found word")
            if self.leafNode:
                return self.center.get_word()
            else:
                return self.center.nav(seqList[1:])
        # horizontal movement - word can be found later alphabetically
        elif condition == -1:
            if self.left is None:
                # print("left node created")
                return self.name
            else:
                return self.left.nav(seqList)
        # horizontal movement - word can be found earlier alphabetically
        else:
            if self.right is None:
                # print("right node created")
                return self.name
            else:
                return self.right.nav(seqList)
