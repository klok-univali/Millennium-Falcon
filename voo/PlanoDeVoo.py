class PlanoDeVoo():

    def __init__(self, rota):
        self.__rota = rota
        self.__baseAtual = rota[0]
        self.__proximaBase = rota[1]

    def obterBaseAtual(self):
        return self.__baseAtual

    def obterProximaBase(self):
        return self.__proximaBase

    def obterRota(self):
        return self.__rota

    def defineNovaRota(self, rota):
        self.__rota = rota
        self.__baseAtual = rota[0]
        self.__proximaBase = rota[1]

    def atualizaProximaBase(self):
        aux = self.__rota.index(self.__proximaBase)+1
        self.__proximaBase = self.__rota[ aux if len(self.__rota) < aux else 0 ]