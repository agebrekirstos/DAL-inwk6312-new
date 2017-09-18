from functools import reduce

def even_sum():
    even_num = []
    for i in range (100 , 500):
        if i%2==0:                   #we can use for i in range (100, 500, 2)
            even_num =even_num + [i] #we can use aso even_num.append(i)
               
            result = reduce((lambda x, y:x+y), even_num)
    return result

print (even_sum())
