class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False


	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca,
			"Modelo: ", self.modelo,  
			"Acelerando: ", self.acelera, 
			"En Marcha: ",self.enmarcha, 
			"Frenando: " , self.frena)

#Nuestra clase Moto, hereda todos los metodos y variables de la clase Vehiculos.
class Moto(Vehiculos):
	pass

miMoto=Moto("Honda", "CBR")

miMoto.estado()
