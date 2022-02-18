def get_pins(o):
    print(o)
    key = {'1':['1','2','4'], '2':['1','2','3','5'], '3':['2','3','6'], 
           '4':['1','4','5','7'], '5':['2','4','5','6','8'], 
           '6':['3','5','6','9'], '7':['4','7','8'],
           '8':['5','7','8','9','0'], '9':['6','8','9'], '0':['0', '8']}
    ans = key[o[0]]
    for i in range(1,len(o)):
        tmp = []
        for j in ans:
            for k in key[o[i]]:
                tmp += [j + k]
        ans = tmp
    return ans

from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins2(observed):
    for n in product(*(ADJACENTS[int(d)] for d in observed)):
        print(n)
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

print(get_pins2('11'))