import math

def confere(l, n):
  s = n
  for i in range(len(l)):
    if (isinstance(l[i], list)):
      s += confere(l[i], s)
    else:
      s += 1  
  return s    
    

def same_structure_as(original, other):
  sz_or = len(original)
  sz_ot = len(other)
  if (sz_or != sz_ot):
    return False
  
  for i in range(sz_or):
    if (isinstance(original[i], list)):
      if (isinstance(other[i], list)):
        if (not(same_structure_as(original[i],other[i]))):
          return False
      else:
        return False
  
  return True
  

original1 = [1, [1, 1]]
other1 = [2, [2, 2]]

original2 = [1, [1, 1]]
other2 = [[2, 2], 2]

original3 = [[[], []]]
other3 = [[[], []]]

original4 = [[[], []]]
other4 = [[1,1]]

print(same_structure_as(original4, other4))
