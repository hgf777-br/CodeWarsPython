def code(s):
    r = ""
    for c in s:
        l = str(bin(int(c))[2:])
        f = "".join(("0" for _ in range(int(len(l))-1)))
        f += "1"
        r += f + l
    
    return r  
    
def decode(s):
    r = ""
    idx = 0
    z = 1
    while (idx < len(s)):
        if (s[idx] != "1"):
            z += 1
            idx += 1
            continue
        idx += 1
        z += idx
        print(z)
        n = ""
        while (idx < z):
            n += s[idx]
            idx += 1
        d = int(n,2)
        r += str(d)
        z = 1
        
    return r

n = "07"
print(n)
print(code(n))
print(decode(code(n)))