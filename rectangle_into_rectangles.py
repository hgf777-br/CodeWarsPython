def rect_into_rects(l, w):
    rect = []
    rect1 = []
    rect2 = []
    quad = []
    mi, ma = (l,w) if l < w else (w, l)
    n = 0
    while(ma > 0):
        if (ma < mi):
            ma, mi = mi, ma
            n = 0
        quad.append(mi)
        if ma > mi:
            rect1.append(f"({ma}*{mi})")
        n += 1
        if n > 1 and ma > mi:
            for i in range(1,n):
                rect1.append(f"({mi*(i+1)}*{mi})")
        ma -= mi
    print(quad)
    print(sorted(rect1))
    
    mi, ma = (l, w) if l < w else (w, l)
    while(mi > 0):
        d = ma // mi
        r = ma % mi
        rect2 += [f"({mi*i}*{mi})" for i in range(2, d+1) for j in range(d+1-i)]
        rect2 += [f"({mi*i+r}*{mi})" for i in range(1, d+1) if r != 0]
        ma = mi
        mi = r

    print(sorted(rect2))
    sz = len(quad)
    for i in range(sz):
        q = quad[i]
        n = q
        j = i + 1
        for j in range(i+1, sz):
            qa = quad[j]
            n += qa
            rect.append(f"({n}*{q})")
            if qa != q:
                break        

    return sorted(rect)

print(rect_into_rects(22, 6))
