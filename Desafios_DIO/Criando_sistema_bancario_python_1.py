import textwrap


def menu():
    menu = '''Escolha umas das seguintes opções:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Lista Contas
    [nu] Novo Usuário
    [q] Sair
    => 
    '''
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('\n === Deposito realizando com sucesseo! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é invalido. @@@')

def sacar(*, saldo, extrato, limite, numero_saque, limite_saque):
def exibir_extrato(saldo, /, *, extrato):
def criar_usuario(usuario):
def filtrar_usuario(cpf, usuario):
def criar_conta(agencia, numero_conta, usuarios):
def listar_contas(contas):
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

main()
