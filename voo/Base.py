import math
import kloklibs.klibmov
from .Localizacao import Localizacao

k = kloklibs.klibmov

class Base():

    def __init__(self, nome, ativa, latitude, longitude):
        self.__nome = nome
        self.__ativa = ativa
        self.__localizacao = Localizacao(latitude, longitude)

    def obterNome(self):
        return self.__nome

    def obterAtiva(self):
        return self.__ativa

    def obterLocalizacao(self):
        return self.__localizacao.obterCoordenadas()

    def obterLocalizacaoObjeto(self):
        return self.__localizacao

    def definirAtiva(self, ativa):
        self.__ativa = ativa

    def distancia(self, localizacao):
        localBase = self.__localizacao.obterCoordenadas()
        localAtual = localizacao.obterCoordenadas()

        return k.disTwoPoints(localBase, localAtual) * 1.113195e5
