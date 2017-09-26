from time import sleep

from sensores.Camera import Camera
from sensores.Microfone import Microfone
from sensores.Quimico import Quimico
from abastecimento.Abastecimento import Abastecimento
from voo.Localizacao import Localizacao
from voo.PlanoDeVoo import PlanoDeVoo
from voo.Velocidade import Velocidade
from voo.Altura import Altura

class Aeronave(object):

    def __init__(self, codigo, rota):
        self.__codigo = codigo
        self.__carga = 50
        self.__planoDeVoo = PlanoDeVoo(rota)
        coord = self.__planoDeVoo.obterBaseAtual().obterLocalizacao()
        self.__localizacao = Localizacao(coord[0], coord[1])
        self.__velocidade=Velocidade()
        self.__altura=Altura()
        self.__camera=Camera()
        self.__microfone=Microfone()
        self.__quimico=Quimico()

    def verificarAbastecimento(self):

        abastecimento=Abastecimento()

        abastecer=abastecimento.abastecer(self.__localizacao.obterCoordenadas(),self.__planoDeVoo.obterProximaBase().obterLocalizacao(),self.__velocidade.obterVelocidade(),self.__carga)

        if abastecer:
            print("Carregando o Drone...")
            print("Carga Atual: %s %%" % self.__carga)

            while(self.__carga < 100):
                self.__carga+=1
                print("Carga Atual: %s %%" %self.__carga)
                sleep(0.5)
            print("Drone Carregado!")
        else:
            print("Carga OK para seguir com o deslocamento!")

    def __desativarSensores(self):
        print("Desligando Camera!")
        self.__camera.desligar()
        print("Desligando Microfone!")
        self.__microfone.desligar()
        print("Desligando Sensor Quimico!")
        self.__quimico.desligar()

    def obterCodigo(self):
        return self.__codigo

    def obterCarga(self):
        return self.__carga

    def obterLocalizacaoAtual(self):
        return self.__localizacao.obterCoordenadas()

    def obterLocalizacaoDestino(self):
        return self.__planoDeVoo.obterProximaBase().obterLocalizacao()

    def definirLocalizacaoAtual(self,latitude,longitude):
        self.__localizacao.definirLatitude(latitude)
        self.__localizacao.definirLongitude(longitude)

    def obterPlanoDeVoo(self):
        return self.__planoDeVoo

    def obterVelocidade(self):
        return self.__velocidade

    def obterAltura(self):
        return self.__altura

    def obterLocalizacao(self):
        return self.__localizacao



