from functools import reduce

def square_of_even ():
    even_num_squared = []
    for i in range (0 , 10):
        if i%2==0:
            i = i**2
            even_num_squared =even_num_squared + [i]
               
            result = reduce((lambda x, y:x+y), even_num_squared)
    return result

print (square_of_even())
