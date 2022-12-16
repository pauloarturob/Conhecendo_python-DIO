import sys  # foi feito a impotação devido a linha 18

# conta_normal = '1'
# conta_universitaria = '2'
#
# saldo = 1000
# cheque_especial = 500


# ------------------------------------------------------------
# 1 exemplo

# saldo = 500
# saque = float(input('Digite o valor para saque: '))
# if saldo >= saque:
#     print('saque realizadio')
# else:
#     print('saldo insuficiente')
# ---------------------------------------------------------

# opcao = int(input('Digite [1] para saque e [2] para extrato\n'
#                   '>> '))
#
# if opcao == 1:
#     valor = float(input('Digite o valor para saque! '))
#     print(f'valor {valor:.2f} sacado com sucesso!')
# elif opcao == 2:
#     print('Exibindo estrato na tela...')
# else:
#     sys.exit('Opção invalida!')

# ---------------------------------------------------------

#--------------------------------Função abaixo para para testes de apreendizagem---------
# def conta_normal():
#     if opcao == 1:
#         saque = float(input('Digite o valor para saque: '))
#         if saldo >= saque:
#             print('Saque realizado com sucesso:')
#         elif saque <= saldo + cheque_especial:
#             print('Saque realizado com uso de cheque especial...')
#     print('Finalizando transação')
#
#
# def conta_universitaria():
#     if opcao == 2:
#         saque = float(input('Digite o valor para saques: '))
#         if saldo >= saque:
#             print('Saque relaizando')
#         else:
#             print('Saldo insuficiente')
#
#
# opcao = int(input('digite a opção desejada,\n[1]Conta normal\n[2]Conta universitaria\n>> '))
# conta_normal()
# conta_universitaria()
#-------------------------------------------------------------------------
 #-----------------------Estrutura ternaria_______________________________

saldo = 2000
saque = 2500
status = 'Seucesso' if saldo >= saque else 'Falha'
print(f'{status} ao realizar o saque...')
