lista = ['P', 'y', 't', 'h', 'o', 'n']

lista[2:] # ['t', 'h', 'o', 'n'] pega do segundo item para frente
lista[:2] # ['P', 'y'] pega do 1 item até o 1
lista[1:3] # ['y', 't']
lista[0:3:2] # ['P', 't']
lista[::] # ['P', 'y', 't', 'h', 'o', 'n'] pega a lista toda
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'P']

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])