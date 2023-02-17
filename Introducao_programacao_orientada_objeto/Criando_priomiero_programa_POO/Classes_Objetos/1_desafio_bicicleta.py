class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plin, Plin')

    def parar(self):
        print('parando bicicleta...')
        print('bicicleta parada')

    def correr(self):
        print('Correndo com a bicicleta')

b1 = Bicicleta('verde', 'fibra', 2023, 50.000)
b1.correr() # acessando dados 
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

