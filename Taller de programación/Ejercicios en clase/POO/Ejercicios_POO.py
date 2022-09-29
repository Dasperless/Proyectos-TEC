class Persona:
	def __init__(self, nombre,apellido,segundo_apellido,año_nacimiento,cedula):
		self.nombre = nombre
		self.apellido = apellido
		self.segundo_apellido=segundo_apellido
		self.año_nacimiento = año_nacimiento
		self.cedula = cedula
	def calcular_edad(self):
		edad=(2018-self.año_nacimiento)
		return edad
	def mostrar_datos(self):
		print("Mi nombre es: ", self.nombre)
		print("Mi primer apellido es: ",self.apellido)
		print("Mi segundo apellido es: ",self.segundo_apellido)
		print("Mi cédula es: ",self.cedula)
class Curso:
        def __init__(self,lista_personas):
                self.lista_estudiantes=lista_personas
        def agregar_estudiantes(self,estudiante):
                self.lista_estudiantes=append(estudiantes)
        def eliminar_estudiantes(self,estudiantes_eliminar):
                for estudiante in self.lista_estudiantes:
                        if estudiante_eliminar.nombre==estudiante.nombre:
                                self.lista_estudiantes.remove(estudiantes)
        def imprimir_estudiantes(self):
                for estudiantes in self.lista_estudiantes:
                        print(estudiantes.nombre)
        def imprimir_estudiantes2(self):
                lista=self.lista_estudiantes
                for i in range(1,len(lista)):
                        pos=i
                        while pos>0 and lista[pos-1].anno_nac>lista[i].anno_nac:
                                pos-=1
                        lista=lista[:pos]+[lista[i]]+lista[pos:i]+lista[i+1:]
                for estudiante in lista:
                        print(estudiante.nombre)
        
        
