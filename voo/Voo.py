import math
import time
import timeit

from .Fases import Fases
from .EspacoAereo import EspacoAereo

import kloklibs.klibmov
k = kloklibs.klibmov

class Voo(Fases):

    def __init__(self):
        pass

    def iniciar(self, drone, espacoAereo):
        v = 1000
        aeronave = espacoAereo.obterAeronave(drone)
        print(aeronave.obterLocalizacaoAtual())

        coordAeronave = aeronave.obterLocalizacaoAtual()
        coordDestino = aeronave.obterPlanoDeVoo().obterProximaBase().obterLocalizacao()

        distancia = k.disTwoPoints([coordAeronave[1],coordAeronave[0]], [coordDestino[1],coordDestino[0]]) * 1.113195e5
        # coefAngular = k.coefAng([coordAeronave[1],coordAeronave[0]], [coordDestino[1], coordDestino[0]])

        tempo = k.timeDisVel(distancia, v)

        tAux = 0
        t1 = tempo
        tempo += timeit.default_timer()

        while tAux < tempo:
            t = t1 - (tempo - timeit.default_timer())
            distanciaProximaBase = distancia - k.disMRU(v, t)

            if distanciaProximaBase < 0:
                distanciaProximaBase = 0

            if (timeit.default_timer() - tAux) > 0.1:
                print("Velocidade: %.3f m/s      Distancia destino: %.3f" % (v, distanciaProximaBase))
                tAux = timeit.default_timer()

    def verificarAbastecimento(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)

        aeronave.verificarAbastecimento()


    def configurar(self, drone, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)

    def subir(self, drone, altura, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)
        aeronave.obterAltura().subir(altura)

    def descer(self, drone, altura, espacoAereo):
        aeronave = espacoAereo.obterAeronave(drone)
        if altura >= 30:
            aeronave.obterAltura.descer(altura)
        else:
            print("Altura mínima permitida durante vôo é de 30m.")
