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
    strip = lambda c : (c if ord(c) in range(97,123)
                                       or c in [",",".","?","!"] else "")
    # cast word to lower and create new string of clean chars
    cleaned = "".join([strip(c) for c in word.lower()])
    return cleaned

def tokenize_text(wordList, tokenList=[]):
    """
    Args: processed word list and list of words consecutive words to tokenize
    Returns: processed word list with tokens as single, multi-word strings
    """
    tokenizedWords = []
    read = True
    for counter, word in enumerate(wordList):
        if word == "borne" and wordList[counter + 1] == "back" and wordList[counter + 2] == "ceaselessly" and read == True:
            tokenizedWords.append(" ".join([word, wordList[counter + 1], wordList[counter + 2]]))
            read = False
        elif read == True:
            tokenizedWords.append(word)
        else:
            read = True
    return tokenizedWords

def process_text(text):
    """
    Args: text
    Returns: list of lowercase, letter-only words in text
    """
    # split text by spacing
    words = text.replace("\n", " ").split(" ")
    # clean all words in list and removed empty strings from cleaning junk
    processedWords = list(filter(None, map(clean_word, words)))
    tokenizedWords = tokenize_text(processedWords)
    return tokenizedWords

def process_text_folder(folder):
    """
    Args: name of folder containing txt files
    Returns: list of all processed words in all texts
    """
    processedWords = []
    for file in os.listdir(folder):
        processedWords += process_text(read_file(f"{folder}/{file}"))
    return processedWords

def process_mutable(sample_name):
    if sample_name.endswith(".txt"):
        type = "file"
        sample = process_text(read_file(sample_name))
    else:
        type = "folder"
        sample = process_text_folder(sample_name)
    return sample, type

print(process_mutable("sample_texts/thegreatgatsby.txt"))
