conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

x = conjunto_a.difference(conjunto_b)
y = conjunto_b.difference(conjunto_a)

print(x) # {1}
print(y) # {4}