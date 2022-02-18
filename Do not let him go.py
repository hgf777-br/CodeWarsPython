from typing import List, Tuple


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    map = {".":1, "#":0, " ":-1}
    m = max((len(x) for x in office))
    mat = [[-1] * (m+2)]
    for o in office:
        mat.append([-1] + [map[x] for x in o] + [-1] * (m - len(o) + 1))   
    mat.append([-1] * (m+2))
    for y in range(1, len(office)+1):
        for x in range(1, m+1):
            if (mat[y][x] == 1):
                if(mat[y-1][x] == -1 or
                  mat[y][x-1] == -1 or
                  mat[y+1][x] == -1 or
                  mat[y][x+1] == -1):
                    return (x-1, y-1)
                
    
    for m in mat:
        print(m)
    
    return 0, 0

print(locate_entrance(['         #######    ', '         #.....#    ', '         #.....#    ', '      ####.....#    ', '      #........#    ', '      #........#    ', '      #........#    ', '      #........#    ', '#######........#####', '#..................#', '##########.........#', '         #.........#', '         #..........', '         ###########']))