import math

def divisors(n):
    div = 1
    for x in range(2,int(n**0.5)+1):
        if (n % x == 0):
            if (n/x == x):
                div += x
            else:
                div += x + n/x            
    return int(div)        

#def divisors(n):
#    return sum((x for x in range(1, int(n**0.5)+1) if not n % x))

def buddy(start,limit):
    for n in range(start, limit + 1):
        sum_n = divisors(n) - 1
        if(sum_n > n):
            sum_m = divisors(sum_n) -1
            if (sum_m == n):
                return [n, sum_n]
    return "Nothing"
       
print(buddy(20,50))
#print(buddy(100,200))
#print(buddy(2177, 4357))
#print(buddy(62700, 62800))
#print(buddy(1071625, 1103735))
