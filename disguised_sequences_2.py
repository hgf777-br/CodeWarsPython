import math


def comb(n, k):
    return int(math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))


def v1(n, p):
    return sum(pow(-1, k)*p*pow(4, n-k)*comb(2*n-k, k) for k in range(n+1))


def u1(n, p):
    return sum(pow(-1, k)*p*pow(4, n-k)*comb(2*n-k+1, k) for k in range(n+1))


def v_eff(n, p):
    return (2*n+1)*p


def u_eff(n, p):
    return (n+1)*p

print(v1(12, 70))
print(u1(13, 18))
print(v_eff(12, 70))
print(u_eff(13, 18))