class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('ligando o motor')

class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def esta_carregado(self):
         print('Nao estou carregado')


moto = Motocicleta('preta', 'abc-1223,', 2)
moto.ligar_motor()

caminhao = Caminhao('roxo', 'ggf-4545', 12)
caminhao.esta_carregado()