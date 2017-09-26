from time import sleep
import timeit
import time

import kloklibs.klibmov
k = kloklibs.klibmov

class Altura():

    def __init__(self):
        self.__mar = 0.0
        self.__solo = 0.0
        self.__velocidade = 2.777  # Velocidade 2.777 m/s  | 10 km/h
        self.__aceleracao = 5.555  # Aceleração 5.555 m/s² | 20 km/h²

    def obterMar(self):
        return self.__mar

    def obterSolo(self):
        return self.__solo

    def subir(self, altura):
        if altura <= 121.0:
            tempoMRUV = k.timeForVel(0, self.__velocidade, self.__aceleracao)
            distanciaMRUV = k.disMRUV(self.__solo, 0, tempoMRUV, self.__aceleracao)
            tempoTotal = tempoMRUV
            t1 = tempoMRUV

            if distanciaMRUV < (altura - self.__solo):
                tempoMRU = k.timeDisVel((altura - self.__solo) - distanciaMRUV, self.__velocidade)
                tempoTotal += tempoMRU
                t2 = tempoMRU
                tempoMRU += (t1 + timeit.default_timer())

            tAux = t = s = sMRUV = v = 0
            tempoMRUV += timeit.default_timer()
            tempoTotal += timeit.default_timer()

            while tAux < tempoTotal:
                if v < self.__velocidade:
                    t = t1 - (tempoMRUV - timeit.default_timer())
                    s = sMRUV = k.disMRUV(self.__solo, 0, t, self.__aceleracao)
                    v = k.velMRUV(0, self.__aceleracao, t)
                else:
                    t = t2 - (tempoMRU - timeit.default_timer())
                    s = k.disMRU(self.__velocidade, t) + sMRUV
                    v = self.__velocidade

                if s > altura:
                    s = altura

                if (timeit.default_timer() - tAux) > 0.1:
                    print("Velocidade: %.3f m/s      Altitude: %.3f m" % (v, s))
                    tAux = timeit.default_timer()

            self.__solo = s
            self.__mar = s + (self.__mar - self.__solo)
        else:
            print("Altura máxima permitida é 121 m.")

    def descer(self, altura):
        if altura >= 0.0:
            distanciaMRU = self.__solo - 10
            tempoMRU = k.timeDisVel(distanciaMRU, self.__velocidade)
            t1 = tempoMRU

            tempoMRUV = k.timeForVel(0, self.__velocidade,self.__aceleracao)
            t2 = tempoMRUV

            tempoTotal = tempoMRU + tempoMRUV

            tAux = t = v = 0
            s = self.__solo
            tempoMRU += timeit.default_timer()
            tempoMRUV += t1 + timeit.default_timer()
            tempoTotal += timeit.default_timer()

            while tAux < tempoTotal:
                if s > 10:
                    t = t1 - (tempoMRU - timeit.default_timer())
                    s = self.__solo - k.disMRU(self.__velocidade, t)
                    v = self.__velocidade
                else:
                    t = t2 - (tempoMRUV - timeit.default_timer())
                    s = k.disMRUV(10, self.__velocidade*-1, t, self.__aceleracao)
                    v = k.velMRUV(self.__velocidade*-1, self.__aceleracao, t) * -1

                if s < 0 or v < 0:
                    s = v = 0

                if (timeit.default_timer() - tAux) > 0.1:
                    print("Velocidade: %.3f m/s      Altitude: %.3f m" % (v, s))
                    tAux = timeit.default_timer()

            self.__solo = s
            self.__mar = s + (self.__mar - self.__solo)
        else:
            print("Altura mínima é o solo.")