import math

import sys

class Abastecimento(object):

    def __init__(self):
        pass

    def abastecer(self,localizacaoAtual,localizacaoFinal,velocidade,carga):

        custo=self.__obterCustoDeslocamento(localizacaoAtual,localizacaoFinal,velocidade)

        if custo > carga and custo <= 100:
            return True
        else:
            return False,False

    def __obterCustoDeslocamento(self,localizacaoAtual,localizacaoFinal,velocidade):

        cargaPorSegundo=(100/60.0)/60.0

        distancia=self.__obterDistanciaEmMetros(localizacaoAtual,localizacaoFinal)

        velocidadeEmMetros=1000/3.6

        tempoDeslocamento=distancia/velocidadeEmMetros

        return tempoDeslocamento*cargaPorSegundo

    def __obterDistanciaEmMetros(self,localizao1, localizao2):
        dlat = localizao2[0] - localizao1[0]
        dlong = localizao2[1] - localizao1[1]
        return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5










