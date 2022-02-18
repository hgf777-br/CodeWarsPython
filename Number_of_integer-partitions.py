def partitions(n):
    if n < 4:
        return n
    p = 2
    ans = 0
    for x in range(n):
        tup = []
        for y in range(p):
            tup.append(n-p+1)
        ans += 1
            
            