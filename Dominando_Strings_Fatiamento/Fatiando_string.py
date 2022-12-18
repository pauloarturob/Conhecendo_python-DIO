nome = 'Paulo Cesar Baeta Artur'

nome[0]
print(nome[0]) # imprime somente uma letra que esta na posição ZERO 'P'

nome[-1]
print(nome[-1]) #imprime a ultima letra da string 'r' 

nome[:5]
print(nome[:5]) #Irá imprimir o estiver ate 5 'Paulo'

nome[12:]
print(nome[12:]) #irá imprimir do 12 pra frente' Baeta Artur

nome[12:16]
print(nome[12:17]) #irá imprimir somente o 'baeta' devido a contagem

nome[12:23:2]
print(nome[12:23:2]) # comença a pega da 12 até a 23 mas pegando pulando de 2 em 2 'BeaAtr'

nome[:]
print(nome[:]) # Imprime a string completa

nome[::-1]
print(nome[::-1]) #colocar a string ao contrario - espelhamento dela