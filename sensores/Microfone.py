from sensores.Sensor import Sensor

class Microfone(Sensor):

    def __init__(self):
        self.__estado=False
        self.__configuracao={'estado':False,'sensibilidade':30}

    def ligar(self):
        self.__configuracao['estado'] = True

    def desligar(self):
        self.__configuracao['estado'] = False

    def configurar(self,configuracao,valor):
        self.__configuracao[configuracao]=valor

    def obterEstado(self,configuracao):
        return self.__configuracao[configuracao]