class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a Calsse...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instancia da Classe...')

    def falar(self):
        print('auau...')

def criar_cachorro():
    c = Cachorro('Zeus', 'Branco e preto', False)
    print(c.nome, c.cor)

criar_cachorro()
c = Cachorro('Romeu', 'preto')
c.falar()
