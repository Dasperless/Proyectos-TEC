import math
class Circulo:
	"""docstring for Ciruclos"""
	def __init__(self, radio):
		self.radio = radio
	def calcular_area(self):
		return math.pi*(self.radio**2)
		
