import math


def windmill(S):
    if len(S) == 1:
        return 0
    if len(S) == 2:
        return 2
    ang = 0
    px = 0
    pa = px
    resp = 0
    while(ang < math.pi*2):
        print('-'*30)
        angulos = []
        Sn = [(x-S[px][0], y-S[px][1]) for (x, y) in S]
        print(Sn)
        for idx, p in enumerate(Sn):
            if(idx != px):
                Dx = p[0]-Sn[px][0]
                Dy = p[1]-Sn[px][1]
                if(Dy == 0):
                    b = math.pi / 2
                else:
                    b = math.atan(Dx/Dy)
                if (p[0] > 0 and p[1] < 0) or (p[0] < 0 and p[1] > 0):
                    b = math.pi + b
                print(idx, b, math.degrees(b))
                b = b - (ang if ang < math.pi else ang - math.pi)
                if idx != pa and b > 0:
                    angulos.append((idx, b))
                elif idx != pa and b < 0:
                    angulos.append((idx, math.pi + b))
        print('-'*30)
        print(angulos)
        print('-'*30)
        atual = min(angulos, key=lambda angulos:angulos[1])
        pa = px
        px = atual[0]
        ang += atual[1]
        resp += 1
        print(px, math.degrees(ang))
    return resp - 1

S = [(0, 0), (2, 1), (-1, 2), (-1, -2)]
#S = [(0, 0), (2, 1), (2, -1), (-2, -1), (-2, 1)]
#S = [(0,0), (1,0)]
#S = [(0, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

print(windmill(S))
