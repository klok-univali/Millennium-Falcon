from abc import ABC, abstractmethod

class Fases(ABC):

    @abstractmethod
    def iniciar(self, drone, espacoAereo):
        pass

    @abstractmethod
    def configurar(self, drone, espacoAereo):
        pass
