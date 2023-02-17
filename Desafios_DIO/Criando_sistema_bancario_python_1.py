import textwrap


def menu():
    menu = '''Escolha umas das seguintes opções:
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tLista Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n === Deposito realizando com sucesseo! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é invalido. @@@')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque
    if excedeu_saldo:
        print('\n@@@ Falhou! Seu saldo é insuficiente! @@@')
    elif excedeu_limite:
        print('\n@@@ Falhou! Valor excede o limite! @@@')
    elif excedeu_saques:
        print('\n@@@ Falhou! Você atingiu o limite de saque por dia! @@@')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saque += 1
        print('\n === Saque realizando!===')
    else:
        print('\n@@@ Operação não realizanda! valor digitado invalido!@@@')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n=============== EXTRATO ===============')
    print('Não foram realizados movimentações.'if not extrato else extrato)
    print(f'\n Saldo: R$ {saldo:.2f}')
    print('=========================================')

def criar_usuario(usuarios):
    cpf = float(input('Informe seu CPF (somente númereos): '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ já existe usuario com esse CPF! @@@')
        return
    nome = input('Informe o seu nome e sobre nome: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro, bairro, cidade-sigla estado')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereço': endereco})
    print('=== Usuario criando com sucesso! ===')
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario [cpf] == cpf]
    return  usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do Usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada correntamente!')
        return {'agencia': agencia, 'numero_conta':numero_conta, 'Usuário': usuario}
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t {conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 80)
        print(textwrap.dedent(linha))
def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = '0001'


    while True:
        opcao = menu()

        if opcao == 'd':
            opcao = opcao.lower()
            valor = float(input('Informe o valor para deposito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            opcao = opcao.lower()
            valor = float(input('Informe o valor para saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break

main()
