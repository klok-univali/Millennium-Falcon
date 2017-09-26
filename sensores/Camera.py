from sensores.Sensor import Sensor

class Camera(Sensor):

    def __init__(self):
        self.__configuracao={'estado':False, 'zoom': 0,'luminosidade': 0,'focoAutomatico': 0,'flash': False}

    def ligar(self):
        self.__configuracao['estado'] = True

    def desligar(self):
        self.__configuracao['estado'] = False

    def configurar(self,configuracao,valor):
        self.__configuracao[configuracao]=valor

    def obterEstado(self,configuracao):
        return self.__configuracao[configuracao]
