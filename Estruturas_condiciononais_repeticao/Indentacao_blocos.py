def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('Valor sacado')
    else:
        print('Limite indisponivel, tente sacar valor menor que o saldo!')

sacar(float(input('Digite o valor para sacar: ')))