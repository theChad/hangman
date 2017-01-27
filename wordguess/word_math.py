"""
Basic entropy calculations for guessing words
"""

import re


def letter_entropy (word, letter, word_list):
    words_with_letter = {x for x in word_list if letter not in x}
    words_sans_letter = {x for x in word_list if letter not in x}


" Based on letters cobbled together so far in word, return all
" remaining possible words.
" word_form is a regular expression containing the letters so far
" word_list is the list of remaining words
def get_possible_words (word_form, word_list):
    """ Return new list of words
    Based on letters cobbled together so far in word, return all
    remaining possible words.
    word_form is a string of letters and .s, e.g. 'h.n..an'
    word_list is the list of remaining words
    """
    word_form += '\b'
    word_form_re = re.compile(word_form)
    new_word_list = {x for x in word_list if word_form_re.match(x)}
    return new_word_list




