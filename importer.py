import os, time
from fnmatch import fnmatch

def read_file(file):
    """
    Args: txt file to read
    Returns: string of contents of txt file
    """
    # check if file is .txt
    if not fnmatch(file, '*.txt'):
        raise ValueError(f"Usage: {file} must be of type .txt")
    # write txt file into string, line by line
    with open(file, encoding = 'utf8') as FileObj:
        text = "".join([line for line in FileObj])
    return text

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

def remove_empty(cleanedWords):
    """
    Args: list of words mapped by clean_word
    Returns: list of words with all empty strings removed
    """
    return [word for word in cleanedWords if word != ""]

def process_text(file):
    """
    Args: txt file to read
    Returns: list of lowercase, letter-only words in file
    """
    text = read_file(file)
    # split text by spacing
    words = text.replace("\n", " ").split(" ")
    # clean all words in words list
    cleanedWords = list(map(clean_word, words))
    # remove all empty strings (products of cleaning pure junk)
    processedWords = remove_empty(cleanedWords)
    return processedWords

def process_text_folder(folder):
    """
    Args: name of folder containing txt files
    Returns: list of all processed words in all texts
    """
    processedWords = [([] + process_text(f"{folder}/{file}") for file in os.listdir(folder))]
    return processedWords

start = time.time()

# sample = process_text('sample_texts/test.pdf')
sample = process_text_folder("sample_texts")

end = time.time()
print(end - start)
