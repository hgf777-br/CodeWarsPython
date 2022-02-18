import re

def valid_parentheses(s):
    ls = re.findall(r'\(|\)',s)
    n = 0
    for x in ls:
        n += 1 if x == "(" else -1
        
    return not n    
    


s = "((())(()))"

print (valid_parentheses(s))

