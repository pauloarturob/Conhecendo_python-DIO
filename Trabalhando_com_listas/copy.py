lista = [1, 'Python', [40, 30, 20]]

lista.copy() # O .copy serve para copiar a lista
print(lista)

# quando e usado o .copy ele somente faz uma copia da lista porem nao altera nada na lista caso haja necessidade de mudar
#alguma coisa ex:

l2 = lista.copy()

print(id(l2), id(lista)) # veja que o id são diferentes : 1960568647872 1960568647552

l2[0] = 2 # nesse caso consigo alterar um item que esta na posição ZERO sem mudar nada na lista :[2, 'Python', [40, 30, 20]]
print(l2)