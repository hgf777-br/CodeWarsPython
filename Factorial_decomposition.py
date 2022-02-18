import math


def decomp(n):
    prime = 2
    next_prime = 0
    first_prime = True
    fat = math.factorial(n)
    ans = ""
    while (fat > 1):
        n = 0
        while(fat % prime == 0):
            n += 1
            fat = fat // prime
        if n != 0: 
            ans += f"{prime}^{n} * " if n != 1 else f"{prime} * "
        if prime == 2:
            prime = 3
        elif first_prime:
            next_prime += 1  
            prime = 6*next_prime-1
            first_prime = False
        else:
            prime = 6*next_prime+1
            first_prime = True
    return ans[:-3]

print(decomp(22))
