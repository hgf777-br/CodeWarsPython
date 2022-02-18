import math
lugares = 9
pessoas = 4
lista1 = [[1],2,3]
lista2 = [[1],2,3]

texto = "Eu fui a praia"

dict1 = { "a": 1, "b": 2}
dict2 = { "a": 3, "b": 4}

def fat(n):
    return 1 if (n == 1 or n == 0) else n*fat(n-1)

def C(n,p):
    return fat(n)/(fat(p)*fat(n-p))

def A(n,p):
    return fat(n)/fat(n-p)

def binomial(n,k,p):
    return C(n,k)*(p**k)*(1-p)**(n-k)

#print(texto[3:])
#print(math.floor(math.log(6,5)))
#print("Combinação: ", C(lugares, pessoas))
#print("Arranjo: ", A(lugares, pessoas))
#print(round(sum(binomial(10,x,0.3) for x in range(3)), 4))

def tst(a):
    a[1] += 5
    return a

#print(tst(lista1.copy()))
#print(lista1)

#print(math.log1p(12))
#print(math.log1p(1))

def f(x):
    return math.expm1(math.log1p(x) / 2)

def f1(x):
    return (x / (math.sqrt(x+1)+1))

#num = 1e-15

#print(f(num))           
#print(f1(num))

f = 269
y =[-298, 281]
#print((f <= y[1]) & (f >= y[0]))

n = "-10"

#print(n.startswith("-")) 
from re import sub

def binary(n):
    return '0' * (n.bit_length()-1) + '1' + bin(n)[2:]

def cipher(mode):
    table = dict((str(d), binary(d))[::mode] for d in range(10))
    return lambda s: sub('|'.join(table), lambda m: table[m[0]], s)

code, decode = cipher(1), cipher(-1)

ls = []
mi = 5
ls += [f"({mi*x}*{mi})" for x in range(1, 3)]

