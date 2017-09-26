from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def configurar(self,configuracao,valor):
        pass

    @abstractmethod
    def obterEstado(self,configuracao):
        pass

