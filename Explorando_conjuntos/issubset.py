conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issubset(conjunto_b)
y = conjunto_b.issubset(conjunto_a)

print(x) # True
print(y) # False
