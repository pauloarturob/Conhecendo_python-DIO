from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adcionar_contas(self, conta):
        self.contas.append(conta)

class PessoaFisica:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\n@@@ Falhou! Seu saldo é insuficiente! @@@')

        elif valor > 0:
            self._saldo -= valor
            print('\n === Saque realizando!===')

            return True

        else:
            print('\n@@@ Operação não realizanda! valor digitado invalido!@@@')


        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\n === Deposito realizando com sucesseo! ===')

        else:
            print('\n@@@ Operação falhou! O valor informado é invalido. @@@')
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes
                             if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print('\n@@@ Falhou! Valor excede o limite! @@@')

        elif excedeu_saques:
            print('\n@@@ Falhou! Você atingiu o limite de saque por dia! @@@')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
        Agencia:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        
    """
class Historico:

    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacoes(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacoes(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacoes(self)