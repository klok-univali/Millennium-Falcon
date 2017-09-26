from time import sleep

from .Fases import Fases
from .EspacoAereo import EspacoAereo

class Decolar(Fases):

    def __init__(self):
        pass

    def iniciar(self, drone, espacoAereo, altura):
        aeronave = espacoAereo.obterAeronave(drone)
        aeronave.obterAltura().subir(altura)

    def configurar(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)
        rota = aeronave.obterPlanoDeVoo().obterRota()

    def verificarAbastecimento(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)

        aeronave.verificarAbastecimento()