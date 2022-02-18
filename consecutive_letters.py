import string

def solve(st):
  return ''.join(sorted(st)) in string.ascii_letters



st = "dacb"
print(sorted(st))
print(''.join(sorted(st)))
print(''.join(sorted(st)) in string.ascii_letters)

print(solve(st))