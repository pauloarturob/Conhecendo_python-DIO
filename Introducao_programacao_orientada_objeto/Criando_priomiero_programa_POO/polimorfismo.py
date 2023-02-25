class Passaro:
    def voar(self):
        print('Pardal vooa')

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não Vooa')

class Aviao(Passaro): # Esse exmplo ruim de herança para 'ganhar' o metodo voar
    def voar(self):
        print('Aviao teco teco decolando ....')
def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())