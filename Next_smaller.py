from itertools import permutations

def next_smaller1(n):
    ns = sorted(str(n))
    if n != int("".join(ns)):
        for x in range(n-1,0,-1):
            if sorted(str(x)) == ns:
                return x
                  
    return -1

def next_smaller2(n):
    ns = str(n)
    no = "".join(sorted(ns))
    if ns == no:
        return -1
    p = permutations(ns,len(ns))
    ans = []
    for x in p:
        xs = "".join(x)
        if (int(xs) < n) and not xs.startswith('0'):
            ans.append(int(xs))

    return -1 if len(ans) == 0 else max(ans)

def next_smaller3(n):
    nl = [x for x in str(n)]
    for x in range(len(nl)-1,0,-1):
        if nl[x-1] == '0':
            nl[x], nl[x-1] = nl[x-1], nl[x]
        elif nl[x] < nl[x-1]:
            nl[x], nl[x-1] = nl[x-1], nl[x]  
            if int("".join(nl)) < n:
                return int("".join(nl))

    return -1

def next_smaller4(n):
    print(n)
    sz = len(str(n))
    for y in range(1,sz):
        nl = [x for x in str(n)]
        for x in range(sz-y,0,-1):  
            nl[x], nl[x-1] = nl[x-1], nl[x]
            if int("".join(nl)) < n and nl[0] != '0':
                return int("".join(nl))
            

    return -1

def next_smaller(n):
    ns = str(n)
    sz = len(ns)
    no = list(ns)
    if no == sorted(no):
        return -1
    n1=0
    for i in range(sz-1,1,-1):
        if no[i] < no[i-1]:
            n1 = i-1
            break
    mx = '0'
    n2 = 0
    for i in range(sz-1,n1,-1):
        if no[i] >= mx and no[i] < no[n1]:
            mx = no[i]
            n2 = i
    print(no)
    no[n1], no[n2] = no[n2], no[n1]
    print(no)
    no = no[:n1+1] + sorted(no[n1+1:], reverse=True)
    print(no)
    return -1 if no[0] == '0' else int("".join(no))

n = 907


#print(next_smaller2(n))
print(next_smaller(n))