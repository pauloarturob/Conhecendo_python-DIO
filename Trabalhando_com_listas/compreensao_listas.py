numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)

# modelo de compreensão
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
# -----------------------------------------------------------------------
# Modificando valores versão 1
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    print(quadrado)

#fazendo compreensão
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)