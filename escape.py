class QUFC:
    def __init__(self, n) -> None:
        self.id = [i for i in range(n)]
        self.sz = [1]*n
    
    def root(self,i) -> int:
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]] # compression path
            i = self.id[i]
        
        return i
        
    def connected(self, p, q) -> bool:
        return self.root(p) == self.root(q)
    
    def union(self, p, q) -> None:
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
            
class QUF:
    def __init__(self, n) -> None:
        self.id = [i for i in range(n)]
        self.sz = [1]*n
    
    def root(self,i) -> int:
        while i != self.id[i]:
            i = self.id[i]
        
        return i
        
    def connected(self, p, q) -> bool:
        return self.root(p) == self.root(q)
    
    def union(self, p, q) -> None:
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]                 

def escape(grid):
    col = len(grid[0])
    row = len(grid)
    board = QUF(col*row)
    full = "".join(grid)
    elements = {b:a for a,b in enumerate(full) if b not in ['.', '#']}
    
    print(row,col)
    print(board.sz)
    print(board.id)
    print(full)
    print(elements)
    
    for i in range(len(full)):
        r = i // col
        c = i - col*r
        print(r,c)
        if full[i] != '#':
            if c + 1 < col and full[i+1] != '#':
                board.union(i,i+1)
            if c - 1 >= 0 and full[i-1] != '#':
                board.union(i,i-1)
            if r + 1 < row and full[i+col] != '#':
                board.union(i,i+col)
            if r - 1 >= 0 and full[i-col] != '#':
                board.union(i,i-col)
                
    print(board.sz)
    print(board.id)
    
    print(board.connected(0,8))
    
    
    
    return []

grid = (
  '.a..',
  '##@#',
  '$A.#'
)

escape(grid)