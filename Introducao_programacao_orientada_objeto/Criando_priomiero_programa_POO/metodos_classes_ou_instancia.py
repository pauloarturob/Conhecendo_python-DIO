#Metodo que usamos com mais frequencia
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
# p = Pessoa('Paulo', 39)
# print(p.nome, p.idade)

#-------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # Metodo de classe
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)

    @staticmethod # Metodo statico
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa.criar_data_nascimento(1983, 3, 38, 'Paulo')
print(p.nome, p.idade)
p2 = Pessoa.e_maior_idade(18)
p3 = Pessoa.e_maior_idade(17)

print(p2, p3)

