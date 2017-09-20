def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(s):
    """This function takes a nested list of strings and returns a new list
       with all the strings capitalized"""
    result = []
    for i in s:
        if isinstance(i,str):
            result = [capitalize_all(i)]
        else:
            result = [capitalize_nested(i)]
    return result

print(capitalize_nested(["print","build", ["this","task"]]))
