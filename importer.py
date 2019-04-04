import os, string

def read_file(file):
    """
    Args: txt file to read
    Returns: string of contents of txt file
    """
    # check if file is of format .txt
    if not file.endswith(".txt"):
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
    strip = lambda c : c if ord(c) in range(97,123) or c in [",",".","?"] else ""
    # cast word to lower and create new string of clean chars
    cleaned = "".join([strip(c) for c in word.lower()])
    return cleaned
def process_text(text):
    """
    Args: text
    Returns: list of lowercase, letter-only words in text
    """
    # split text by spacing
    words = text.replace("\n", " ").split(" ")
    # clean all words in list and removed empty strings from cleaning junk
    processedWords = list(filter(None, map(clean_word, words)))
    return processedWords

def process_text_folder(folder):
    """
    Args: name of folder containing txt files
    Returns: list of all processed words in all texts
    """
    processedWords = []
    for file in os.listdir(folder):
        processedWords += process_text(read_file(f"{folder}/{file}"))
    return processedWords


sample = process_text_folder("sample_texts")

print(sample[0:300])
