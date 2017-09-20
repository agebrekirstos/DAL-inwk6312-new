import string
import functools

def read_book():
    """This function reads a book from file, strips punctuation and space,
    and converts them to lowercase"""
    
    f = open("74-0.txt")
    p = string.punctuation
    c = 0
    for line in f:
        ln = line.replace('-',' ')
        for w in ln.split():
            #c = line.count(w)
            w = w.lower()
            w = w.strip(p)
            c+=1
            new_word=""
            for let in w:
                if let not in p:
                    new_word+=let
            #print(new_word)
    print(c)

read_book()
