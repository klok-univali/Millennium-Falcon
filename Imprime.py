import time

class Imprime():
	
	def __init__(self):
		self.__num = 500
		
	def incrementa(self):
		i = 0
		while i < 10:
			self.__num+=10
			print(str(self.__num) + "interno")
			time.sleep(1)
			i+=1