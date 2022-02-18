def testit(s):
    ans=""
    for a,b in zip(s[0::2], s[1::2]):
        ans += chr(ord(min(a,b)) + abs(ord(a)-ord(b)) // 2)
    
    if (len(s)%2 != 0):
        ans += s[-1:]    
    return ans    

print (testit("hheellllo"))