class NailingABanner:
    def coordinate(self, n):
        co = [0, 2**60]
        if n < 3:
            return co[n-1]
        i = 1
        sz = len(co)
        while (n > 2):
            new = (co[i] - co[i-1]) / 2
            co.insert(i, new)
            i += 2
            if i < sz:
                i = 1
                sz = len(co)
            n -= 1
        
        return co


nail = NailingABanner()
print(nail.coordinate(1))
print(nail.coordinate(2))
print(nail.coordinate(3))
print(nail.coordinate(4))
print(nail.coordinate(5))
