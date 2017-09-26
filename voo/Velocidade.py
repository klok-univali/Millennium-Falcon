from time import sleep

class Velocidade():

    def __init__(self):
        self.__velocidade = 0.0
        self.__aceleracao = 0.0

    def obterVelocidade(self):
        return self.__velocidade

    def acelerar(self, velocidade):
        if velocidade > self.__velocidade:
            self.__aceleracao = 18.0
            auxVel = self.__velocidade
            tempo = 1;

            while self.__velocidade < velocidade:
                self.__velocidade = auxVel + (self.__aceleracao * tempo)
                if self.__velocidade > velocidade:
                    self.__velocidade = velocidade

                print(str(self.__velocidade) + " m/s")
                tempo+=1
                sleep(1)

            self.__aceleracao = 0.0
        else:
            print("Velocidade atual é superior a %s m/s." %velocidade)

    def desacelerar(self, velocidade):
        if velocidade < self.__velocidade:
            self.__aceleracao = -18.0
            auxVel = self.__velocidade
            tempo = 1;

            while self.__velocidade > velocidade:
                self.__velocidade = auxVel + (self.__aceleracao * tempo)
                if self.__velocidade < velocidade:
                    self.__velocidade = velocidade

                print(self.__velocidade)
                tempo+=1
                sleep(1)

            self.__aceleracao = 0.0
        else:
            print("Velocidade atual é inferior a %s m/s." %velocidade)