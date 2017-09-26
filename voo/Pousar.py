from time import sleep

from .Fases import Fases
from .EspacoAereo import EspacoAereo

class Pousar(Fases):

    def __init__(self):
        pass

    def iniciar(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)
        aeronave.obterAltura().descer(0)

    def configurar(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)
        #rota = aeronave.obterPlanoDeVoo().obterRota()
