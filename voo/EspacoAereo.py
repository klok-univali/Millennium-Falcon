import json

from .Base import Base
from .Aeronave import Aeronave

class EspacoAereo():

    def __init__(self):
        self.__codAeronave = 1;
        self.__aeronaves = {}
        self.__bases = []
        bases = json.load(open("penitenciarias.json"))

        for i in range(len(bases)):
            base = Base(bases[i]['Nome'], True, bases[i]['Latitude'], bases[i]['Longitude'])
            self.__bases.append(base)

    def __adicionaAeronave(self, drone):
        self.__aeronaves[drone] = Aeronave(self.__codAeronave, self.__bases)
        self.__codAeronave+=1

    def obterAeronave(self, drone):
        if drone not in self.__aeronaves:
            self.__adicionaAeronave(drone)

        return self.__aeronaves.get(drone)

    def obterBases(self):
        return self.__bases