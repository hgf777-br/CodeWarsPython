from decimal import Decimal


def quadratic(a, b, c):
    A = Decimal(str(a))
    B = Decimal(str(b))
    C = Decimal(str(c))
    dois = Decimal('2')
    quatro = Decimal('4')
    meio = Decimal('0.5')
    
    D = (B**dois - quatro*A*C)
    x1 = (-B + D**meio) / (dois*A)
    x2 = (-B - D**meio) / (dois*A)
    
    print('\nValor de x1: {0}'.format(x1))
    print('Valor de x2: {0}'.format(x2))
    
    x = float(x1) if abs(x1) < abs(x2) else float(x2)
    
    x = x*1.75
    
    atual = a * x * x + b * x + c
    
    print(x, atual)
    
    return x1 if abs(x1) < abs(x2) else x2


#print(quadratic(5,4e+15,5))
#print(quadratic(3,3e+11,3))
root = quadratic(5, 4e+14, 7)