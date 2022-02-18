def valid_number(n):
    print(n)
    p = n.find('.')
    if (p < 0):
        return False
    a = n[:p]
    b = n[p+1:]
    if (a.startswith("-") or a.startswith("+")):
        a = a[1:]
    print(a,b)
    if (not a.isdecimal() and not a == ""):
        print("vazio")
        return False 
    if (not (b.isdecimal())):
        return False
    if (len(b) == 2):
        return True
    
    return False
    
print(valid_number("-1.40"))