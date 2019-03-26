import string

def clean_word(word):
    """
    Args: raw word
    Returns: lowercase, letter-only word
    """
    # lambda to discard char if not lowercase letter
    strip = lambda c : c if ord(c) in range(97,123) else ""
    lowerWord = word.lower()

    for c in word:
        strip(c)

def process_text(text):
    """
    Args: string of all words in a text
    Returns: list of lowercase, letter-only words
    """
    strip = lambda c : c if ord(c) in range(97,123) else ""

    wordList = text.split(" ")

    for word in wordList:
        for char in word:
            store += strip(char)

    print(store)

# process_text("4 5 3 1")


x = string.maketrans("","")
