import math
from decimal import Decimal

def mant_exp(a_number, digits_number):
    exp_orig = Decimal(str(math.floor(Decimal.log10(a_number))))
    matissa = int(a_number * (Decimal(10) ** (exp_orig * Decimal(-1))) * (Decimal(10) ** (Decimal(digits_number) - Decimal(1))))
    exp = exp_orig - digits_number + 1 
    return ''.join([str(matissa), 'P', str(exp)])
    
print(mant_exp(Decimal("0.06"), 10))
#print(mant_exp(Decimal("72.0"), 12))
#print(mant_exp(Decimal("1.0"), 5))
#print(mant_exp(Decimal("123456.0"), 4))