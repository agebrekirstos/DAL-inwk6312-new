import string
import functools

def read_book():
    """This function reads a book from file, strips punctuation and space,
    and converts them to lowercase"""
    
    f = open("74-0.txt")
    p = string.punctuation
    for line in f:
        for w in line.split():
            w = w.lower()
            w = w.strip(p)
            new_word=""
            for let in w:
                if let not in p:
                    new_word+=let
            print(new_word)

read_book()
