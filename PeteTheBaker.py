import math

def cakes(recipe, available):
  cakes = 0
  stock = available
  while(True):
    for re in recipe:
      av = stock.get(re, -1)
      if (av > 0 and stock[re] - recipe[re] >= 0):
        stock[re] = stock[re] - recipe[re]
      else:
        return cakes;
      print(av, stock[re])
    cakes += 1
  
  return -1


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}

recipe = {'cream': 1, 'flour': 3, 'sugar': 1, 'milk': 1, 'oil': 1, 'eggs': 1}
available = {'sugar': 1, 'eggs': 1, 'flour': 3, 'cream': 1, 'oil': 1, 'milk': 1}
print('Bolos ', cakes(recipe, available))
