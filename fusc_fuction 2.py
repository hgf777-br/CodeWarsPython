def fusc_list():
    n = 1
    d = 1
    yield (n, d)
    while True:
        n, d = d, 2 * (n // d) * d + d - n
        yield (n, d)

def fusc(n):
    f = 0
    for i in fusc_list(): 
        f = i
        n -= 1
        if n < 2:
            break
            
    return f[1]

print(fusc(111111111))    