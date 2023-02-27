from abc import ABC, abstractmethod, abstractproperty

class ControleRemnoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca(self):
        pass
class Controletv(ControleRemnoto):
    def ligar(self):
        print('Ligando a TV....')
    def desligar(self):
        print('Desligando tv ...')
    @property
    def marca(self):
        return 'LG'

class ControleArCondicionado(ControleRemnoto):
    def ligar(self):
        print('Ligando a AR....')
    def desligar(self):
        print('Desligando AR ...')
    @property
    def marca(self):
        return 'LG..'




controle = Controletv()

controle.ligar()
controle.desligar()
print(controle.marca)

ar = ControleArCondicionado()
ar.ligar()
ar.desligar()
print(ar.marca)
