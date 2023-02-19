class Estutande:
    escola = 'Dio'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome}- {self.matricula} - {self.escola}'

aluno1 = Estutande('Paulo', 1)
aluno2 = Estutande('Stefanie', 2)

print(f'o aluno(a): {aluno1} e o anluno(a): {aluno2}')

