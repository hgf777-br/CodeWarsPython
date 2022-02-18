def hamilton(G, size, pt, path = []):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
        
        
def square_sums_row(n):
    
    quadrados = []
    for i in range(2, int(n/2)+1):
        quadrados.append(i**2)
    
    duplas = []
    for x in range(1, n+1):
        for y in range(1, n+1):
            if x + y in quadrados and x != y:
                duplas.append((x, y))
                
    print(quadrados)       
    print(duplas)
    exit()
    grafo = {}
    for x in duplas:
        if x[0] not in grafo:
            grafo[x[0]] = [x[1]]
        else:
            grafo[x[0]].append(x[1])
        
    print(quadrados)
    print(grafo)
    resultado =[]
    for x in range(1,n+1):
        print(f"Inicio {x} --------")
        resultado = hamilton(grafo, n, x, [])
        if resultado != None:
            return resultado
    
    return False

n = 43

print("Final : ", square_sums_row(n))