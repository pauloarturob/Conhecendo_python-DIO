# Exemplo de dados publicos e privados

# class Conta:
#     def __init__(self, saldo=0)
#         self._saldo = saldo  #veja no antes do self._saldo há um anderline que indica que essa variavel e privada
#
#     def depositar(self, valor):
#         pass  # aqui a variavel é publica
#
#     def sacar(self, valor):
#         pass  # aqui a variavel é publica

#-------------------------------------------------------------------------------------------
#
# class Conta:
#     def __init__(self, nro_agencia, saldo=0):
#         self._saldo = saldo
#         self.nro_agencia = nro_agencia
#
#     def depositar(self, valor):
#         pass
#
#     def sacar(self, valor):
#         pass
#
#     def mostrar_saldo(self):
#         return self._saldo
#
# conta = Conta('0001', 100)
# conta.depositar(100)
# print(conta.nro_agencia)
# print(conta.mostrar_saldo())

#------------------------------------------------------------------------------------------------

#Propriedade

# class Foo:
#     def __init__(self, x=None):
#         self._x = x
#
#     @property
#     def x(self):
#         return self._x or 0
#
#     @x.setter
#     def x(self, value):
#         _x = self._x or 0
#         _value = value or 0
#         self._x = _x + _value
#
#     @x.deleter
#     def x(self):
#         self._x = -1
#
# foo = Foo(10)
# print(foo.x)
# foo.x = 10
# print(foo.x)
# del foo.x
# print(foo.x)

#------------------------------------------------------------------------------------------------
#Outro exemplo

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    # @property
    # def nome(self): # como o nome nao tem função e esta somente retornando não precisa de um @property
    #     return self._nome

    @property
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa(input('Nome: '), int(input('Ano de nascimento: ')))
print(f'Nome: {pessoa._nome} \tIdade: {pessoa.idade}')