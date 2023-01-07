conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issuperset(conjunto_b)
y = conjunto_b.issuperset(conjunto_a)

print(x) # False
print(y) # True