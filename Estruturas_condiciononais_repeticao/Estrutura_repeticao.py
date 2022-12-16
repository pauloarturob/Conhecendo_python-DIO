# # Reeceba um número do teclado e exiba os 2 numeros seguintes. ex simples
#
# a = int(input('Digite seu numeros: '))
#
# a += 1
# print(a)
# a += 1
# print(a)

# --------------------------------------------------------------------
# ----------Estrutura FOR utilizando um iterável-----------------

# texto = input('Digite seu texto ')
# vogais = 'AEIOU'
#
# for letra in texto:
#     if letra.upper() in vogais:
#         print(letra, end= '')


# --------------------------------------------------------------------
# ----------Estrutura Função Range função bult-in range-----------------
#
# for x in range(0, 3):
#     print(x)
#
# #fazendo um tabuada de 5
#
# for y in range(0, 51, 5):
#     # print(y) #sem end no final fica em linha vertical
#     print(y, end=' ') # agora a sequencia ficara em horizontal

# --------------------------------------------------------------------
# ----------Estrutura Função while-----------------

# opcao = -1
#
# while opcao != 0:
#     opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n>> '))
#
#     if opcao == 1:
#         print('Sacando...')
#     elif opcao == 2:
#         print('Exibindo extrato...')
#
#
# else:
#     print('Obrigado volte sempre')

# --------------------------------------------------------------------
# ----------Estrutura Função while----usando Break-------------

opcao = -1

while True:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n>> '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')
    elif opcao == 0:
        break
else:
    print('Obrigado volte sempre')

