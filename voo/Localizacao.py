class Localizacao():

    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    def obterCoordenadas(self):
        return [self.__latitude, self.__longitude]

    def definiLatitude(self, latitude):
        self.__latitude = latitude

    def definiLongitude(self, longitude):
        self.__longitude = longitude