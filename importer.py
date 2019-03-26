import string
from datetime import datetime
import re

def clean_word(word):
    """
    Args: raw word
    Returns: lowercase, letter-only word
    """
    # lambda to discard char if not lowercase letter
    strip = lambda c : c if ord(c) in range(97,123) else ""
    # cast word to lower and create new string of clean chars
    cleaned = "".join([strip(c) for c in word.lower()])
    return cleaned

def read_file(file):
    """
    Args: .txt file to read
    Returns: string of contents of .txt file
    """
    with open(file) as FileObj:
        text = "".join([line + " " for line in FileObj])
    return text

def process_text(file):
    """
    Args: .txt file to read
    Returns: list of lowercase, letter-only words in file
    """
    text = read_file(file)
    # split text by spacing
    # words = text.split(" ")
    words = re.split(" |\n", text)
    print('past')
    # clean all words in words list
    processedWords = list(map(clean_word, words))
    # remove all individual spaces from processWords
    while "" in processedWords:
        processedWords.remove("")
    return processedWords

start=datetime.now()

sample = process_text("sample_texts/warandpeace.txt")

print(sample)

print(datetime.now()-start)
