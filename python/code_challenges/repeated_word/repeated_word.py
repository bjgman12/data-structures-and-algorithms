# from linked_list import Node,LinkedList
from hashtable import Hashtable
import string

def repeated_word_check(text_to_check):
    case_format = text_to_check.lower()
    punctuation_clean = case_format.translate(str.maketrans('','',string.punctuation))
    iterable_words = punctuation_clean.split()
    ht = Hashtable()

    for word in iterable_words:
        if ht.contains(word):
            return word
        else:
            ht.set(word,word)
    return 'No Words Repeated'