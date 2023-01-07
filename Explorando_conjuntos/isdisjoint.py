conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

x = conjunto_a.isdisjoint(conjunto_b)
y = conjunto_a.isdisjoint(conjunto_c)

print(x) # True
print(y) # False

# E quando os valor que tem em um conjunto nao tem em outro conjunto!