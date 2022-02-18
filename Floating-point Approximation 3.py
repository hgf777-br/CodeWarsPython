import math

def quadratic(a, b, c):
    
    D = math.sqrt(b**2 - 4*a*c)
    sg = 1 if b > 0 else -1
    x1 = (-b - sg * D) / 2 * a
    x2 = 2 * c / (-b - sg * D)
    
    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))
    
    x  = float(x1) if abs(x1) < abs(x2) else float(x2)
    
    atual = a * x * x + b * x + c
    
    print (x, atual)
    
    return x1 if abs(x1) < abs(x2) else x2


#print(quadratic(5,4e+15,5))
#print(quadratic(3,3e+11,3))
root = quadratic(5,4e+14,7)