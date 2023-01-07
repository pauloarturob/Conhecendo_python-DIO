lista = [1, 2, 4, 66, 78]
print(lista)

lista.append(int(input('Insira o valor desejado: ')))

lista.sort()
print(lista)
lista.extend(int(input('Digite mais: ')))

remover = (int(input('Digite o numero a ser removido: ')))

if remover in lista:
    lista.remove(remover)
    print(f'O numero {remover} foi encotrado e deletado\n'
          f'veja a a lista: {lista}')
else:
    print(f'numero {remover} não foi encontrado!')

print(f'Contem {len(lista)} numeros na lista')
