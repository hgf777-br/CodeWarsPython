def draw(waves):
    m = max(waves)
    l = len(waves)
    ls = ['□'*l]*m
    idx = 0
    for w in waves:
        for p in range(1,w+1):
            ls[m-p] = ls[m-p][:idx] + '■' + ls[m-p][idx+1:]
        idx += 1    
            
    print(ls)
    return "\n".join(ls)


waves = [1,2,3,4]
waves = [1,2,3,3,2,1]

print(draw(waves))