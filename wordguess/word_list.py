"""
Class for importing word list
"""

class WordList:
    def __init__(self, word_list_filename):
        with open(word_list_filename) as f:
            self.word_list = set(line.strip() for line in f.read())


