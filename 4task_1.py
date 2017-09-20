def nested_sum (t):
    total = 0
    for i in t:
        if isinstance(i,int):
            total+=i
        
        else:
           total+= nested_sum(i)
    return total
            
        

print(nested_sum([1,2,[3,4]]))
