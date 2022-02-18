def sum_of_intervals(intervals):
    vals = []
    vals.append([intervals[0][0], intervals[0][1]])
    for x in range(1, len(intervals)):
        item = [intervals[x][0], intervals[x][1]]
        vals.append(item)
        vals.sort(key=lambda x: x[0])
        idx = vals.index(item)
        
        y = idx - 1
        while (y > -1):
            if (item[0] <= vals[y][1] and item[0] >= vals[y][0]):
                if(item[1] <= vals[y][1]):
                    vals.pop(idx)
                    idx -= 1
                else:
                    vals[y][1] = item[1]
                    item = vals[y]
                    vals.pop(idx)
                    idx -= 1
            if (item[0] < vals[y][0]):
                if (item[1] <= vals[y][1] and item[1] >= vals[y][0]):
                    vals[y][0] = item[0]
                    item = vals[y]
                    vals.pop(idx)
                    idx -= 1
                elif (item[1] > vals[y][1]):
                    vals[y] = item
                    vals.pop(idx)
                    idx -= 1
            y -= 1                
                   
        y = idx + 1
        while (y < len(vals)):
            if (item[1] <= vals[y][1] and item[1] >= vals[y][0]):
                if(item[0] >= vals[y][0]):
                    vals.pop(idx)
                    y -= 1
                else:
                    vals[y][0] = item[0]
                    vals.pop(idx)
                    y -= 1
            if (item[1] > vals[y][1]):
                if (item[0] <= vals[y][1] and item[0] >= vals[y][0]):
                    vals[y][1] = item[1]
                    vals.pop(idx)
                    y -= 1
                elif (item[0] < vals[y][0]):
                    vals[y] = item
                    vals.pop(idx)
                    y -= 1
            y += 1    
        
    ans = 0
    for x in vals:
        ans += x[1] - x[0]
                                
    return ans

intervals = [
   [1, 2],
   [6, 10],
   [11, 15]
]

intervals = [
   [1, 4],
   [7, 10],
   [3, 5]
]

intervals = [
    (-298, 281),
    (-50, 269),
    (-76, 200),
    (321, 422),
    (224, 463),
    (-495, -333),
    (-283, 77)
]

intervals = [
    (484, 490),
(336, 409),
(-345, 166),
(421, 482),
(234, 414),
(-345, 344),
(368, 478),
(-261, 325)
]

intervals = [
    (444, 481), 
    (345, 396), 
    (-182, 285), 
    (-430, -286), 
    (463, 477), 
    (-415, 467), 
    (279, 319), 
    (-420, -355), 
    (340, 410)
    ]

print(sum_of_intervals(intervals))