menu = '''Escolha umas das seguintes opções:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        opcao = opcao.lower()
        valor = float(input('Informe o valor para deposito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('Operação falhou! O valor informado é invalido...')

    elif opcao == 's':
        opcao = opcao.lower()
        valor = float(input('Informe o valor para saque: '))

        execedeu_saldo = valor > saldo
        execedeu_limite = valor > limite
        execedeu_saques = valor >= LIMITE_SAQUES

        if execedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif execedeu_limite:
            print('Operação falhou! O valor de saque excede o limite.')
        elif execedeu_saques:
            print('Operação falhou! Número de limtes de saques excedido!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Operação falhou! o valor informado é invalido.')
    elif opcao == 'e':
        opcao = opcao.lower()
        print('=======================Extrato=======================')
        print('foram realizados movimentações.'if not extrato else extrato)
        print(f'\n Saldo : R$ {saldo:.2f}')
        print('======================================================')

    elif opcao == 'q':
        opcao = opcao.lower()
        break
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada...')
