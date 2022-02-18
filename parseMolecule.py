def parse_molecule(formula):
  mols = []
  final = {}
  subs_1 = []
  subs_2 = []
  subs_3 = []
  idx = 0
  id = 0      
  while id <  len(formula):
    c = formula[id]
    if (c.isalpha()):
      if (c.islower()):
        mols.pop()
        c_temp += c
        mols.append([c_temp,1])
      else:
        mols.append([c,1])
        c_temp = c
        idx += 1
    if (c.isnumeric()):
      num = int(c)
      if id < (len(formula) - 1):
        while(formula[id + 1].isnumeric()):
          num = num*10 + int(formula[id + 1])
          id += 1
      mols[len(mols)-1][1] *= num
    if (c == '('):
      subs_1.append([idx,0,1])
    if (c == '['):
      subs_2.append([idx,0,1])
    if (c == '{'):
      subs_3.append([idx,0,1])    
    if (c == ')'):
      subs_1[len(subs_1) - 1][1] = idx
      if formula[id + 1].isnumeric():
        id += 1
        num = int(formula[id])
        if id < (len(formula) - 1):
          while(formula[id + 1].isnumeric()):
            num = num*10 + int(formula[id + 1])
            id += 1
        subs_1[len(subs_1) - 1][2] = num
      else:
        subs_1[len(subs_1) - 1][1] = idx
    if (c == ']'):
      subs_2[len(subs_2) - 1][1] = idx
      if formula[id + 1].isnumeric():
        id += 1
        num = int(formula[id])
        if id < (len(formula) - 1):
          while(formula[id + 1].isnumeric()):
            num = num*10 + int(formula[id + 1])
            id += 1
        subs_2[len(subs_2) - 1][2] = num
      else:
        subs_2[len(subs_2) - 1][1] = idx
    if (c == '}'):
      subs_3[len(subs_3) - 1][1] = idx
      if formula[id + 1].isnumeric():
        id += 1
        num = int(formula[id])
        if id < (len(formula) - 1):
          while(formula[id + 1].isnumeric()):
            num = num*10 + int(formula[id + 1])
            id += 1
        subs_3[len(subs_3) - 1][2] = num
      else:
        subs_3[len(subs_3) - 1][1] = idx     
    id += 1
  
  print(mols)
  print(subs_1)
  print(subs_2)
  print(subs_3)
  
 
  for id in range((len(subs_1) - 1), -1, -1):
    for x in range(subs_1[id][0], subs_1[id][1]):
      mols[x][1] *= subs_1[id][2]
  for id in range((len(subs_2) - 1), -1, -1):
    for x in range(subs_2[id][0], subs_2[id][1]):
      mols[x][1] *= subs_2[id][2]
  for id in range((len(subs_3) - 1), -1, -1):
    for x in range(subs_3[id][0], subs_3[id][1]):
      mols[x][1] *= subs_3[id][2]  
  
  print(mols)
  
  for s in mols:
    if final.get(s[0]):
      final[s[0]] += s[1]
    else:  
      final[s[0]] = s[1]
      
  return final

molecule = "H2O"
molecule = "Mg(OH)2"
molecule = "K4[ON(SO3)2]2"
#molecule = "C6H12O6"
#molecule = "(C5H5)Fe(CO)2CH3"
molecule = "{[Co(NH3)4(OH)2]3Co}(SO4)3"

print(parse_molecule(molecule))