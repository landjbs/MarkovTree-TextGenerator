import string

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

def process_text(text):
    """
    Args: string of all words in a text
    Returns: list of lowercase, letter-only words
    """
    strip = lambda c : c if ord(c) in range(97,123) else ""

    wordList = text.split(" ")
