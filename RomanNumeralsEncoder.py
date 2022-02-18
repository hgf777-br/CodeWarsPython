def solution(n):
    romans = [("I", "V", "X"), ("X", "L", "C"), ("C", "D", "M"), ("M")]
    ans = ""
    idx = 0
    while (n > 0):
        d = n % 10
        if d != 0:
            if d <= 3:
                ans = romans[idx][0]*d + ans
            elif d <= 8:
                ans = romans[idx][0]*(d-3)*(5-d) + romans[idx][1] + romans[idx][0]*(d-5) + ans
            else:
                ans = romans[idx][0] + romans[idx][2] + ans
        idx += 1
        n //= 10

    return ans


x = 3999
print(x, solution(x))
