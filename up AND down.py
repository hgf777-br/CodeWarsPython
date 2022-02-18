def arrange(s):
    l = s.split()
    size = len(l)
    done = False
    while(not done):
        g = True
        for i in range(size-1):
            if g and len(l[i]) > len(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
                break
            elif not g and len(l[i]) < len(l[i+1]):        
                l[i], l[i+1] = l[i+1], l[i]
                break
            g = not g
            
        g = True
        done = True
        for i in range(size-1):
            if g and len(l[i]) > len(l[i+1]):
                done = False
                break
            elif not g and len(l[i]) < len(l[i+1]):        
                done = False
                break
            g = not g    
            
    g = True
    for i in range(size):
        if not g:
            l[i] = l[i].upper()
        else:
            l[i] = l[i].lower()
        g = not g
        
    return " ".join(l)        
    
s = "who hit retaining The That a we taken"
print(arrange(s))    