import math

def interp(f, l, u, n):
    resposta = [math.floor(f(l)*100)/100]
    for i in range(1, n):
        d = (u - l) / n
        print(d)
        #resposta.append(math.trunc(f(l + i * d)*100)/100)
        resposta.append(math.floor(f(l + i * d)*100)/100)
    return resposta
#print(interp(lambda x : x, 0, 9.0, 4))
#print(interp(lambda x : x, 0, 15.0, 9))
print(interp(lambda x : math.sin(x), 0, 18.0, 12))