from tkinter import *
import random
#Globales
global ambientacion,nombreJugador1,nombreJugador2,matrizMultijugador1,matrizMultijugador2, matrizvsComputadora
ambientacion   = 0
nombreJugador1 = "Jugador 1"
nombreJugador2 = "Jugador 2"

"""MATRICES DE LOS TABLEROS"""
matrizMultijugador1  = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]]

matrizMultijugador2  = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]]

matrizvsComputadora  = [[0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0]]

"""EMBARCACIONES"""
global portaavionesJugador1,portaavionesJugador2,buqueJugador1,buqueJugador2,lanchaJugador1,labelJugador2
	#Embarcaciones Jugador 1
portaavionesJugador1 = 2
buqueJugador1 = 3
lanchaJugador1 = 4

	#Embarcaciones Jugador 2
portaavionesJugador2 = 2
buqueJugador2 = 3
lanchaJugador2 = 4

global portaavionesVsComputadora,buqueVsComputadora,lanchaVsComputadora
	#Embarcaciones vs Computadora
portaavionesVsComputadora= 2
buqueVsComputadora = 3
lanchaVsComputadora = 4

	#TURNO DE MULTIJUGADOR
global Turno 
turno = 1


class Ventana:
	def __init__(self,main):
		self.main = main

	def ambiente(self):
		global ambientacion
		if ambientacion == 0:
			photo = PhotoImage(file="pacifico_central.png")
			background_label = Label(self.main, image=photo)
			background_label.place(x=0, y=0, relwidth=1, relheight=1)
			background_label.image = photo
		elif ambientacion == 1:
			photo = PhotoImage(file="Piratas_caribe.png")
			background_label = Label(self.main, image=photo)
			background_label.place(x=0, y=0, relwidth=1, relheight=1)
			background_label.image = photo
		elif ambientacion == 2 :
			photo = PhotoImage(file="Polo_norte.png")
			background_label = Label(self.main, image=photo)
			background_label.place(x=0, y=0, relwidth=1, relheight=1)
			background_label.image = photo
		elif ambientacion == 3 :
			photo = PhotoImage(file="Vikingos.png")
			background_label = Label(self.main, image=photo)
			background_label.place(x=0, y=0, relwidth=1, relheight=1)
			background_label.image = photo			

	def tableroMultijugador(self):
		global nombreJugador1,nombreJugador2,turno
		self.main.state("zoomed")
		"""Nombres del tablero"""
		labelJugador1 = Label(self.main,text=nombreJugador1)
		labelJugador1.place(x=262,y=70)
		labelJugador1.config(font=("Courier", 16))

		labelJugador2 = Label(self.main,text=nombreJugador2)
		labelJugador2.place(x=1000,y=70)
		labelJugador2.config(font=("Courier", 16))


		botonReiniciar = Button(self.main,text="Reiniciar juego",command=lambda: self.reiniciarJuego()).place(x=0,y=560)



		""" NUMEROS DEL TABLERO 1 """

		#Variables 
		cordx=62
		cordy=100

		#incrementos de las variables
		incordx=52

		for i in range(1,11):
			var=StringVar()
			labelNumeros={}
			labelNumeros["string{0}".format(i)]=Button(self.main,text=i, width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
			var.set(i)
			cordx+=incordx

		""" LETRAS DEL TABLERO 1"""

		#Lista con las letras que se encuentran en el tablero
		letras=["A","B","C","D","E","F","G","H","J","K"]

		#Variables
		m=1
		cordx=10
		cordy=140

		#Incrementos
		incordy=40
		incm=1

		for l in letras:
		    tempLetra=letras[m-1]
		    var=StringVar()
		    labelNumeros={}
		    labelNumeros["string{0}".format(l)]=Button(self.main,text=tempLetra,width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
		    var.set(l)
		    m+=incm
		    cordy+=incordy

		""" BOTONES DEL TABLERO 1"""

		#Variables
		cordx=62
		cordy=140

		#Incrementos
		incordy=40
		incordx=52

		#Constante
		conCordx=62

		for i in range(10):
			for j in range(10):
				boton={}
				boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2,command=lambda i=i, j=j,cordx=cordx,cordy=cordy:self.valTablero([i,j],1,cordx,cordy))
				boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		""" NUMEROS DEL TABLERO 2 """

		#Variables
		cordx = 800
		cordy = 100

		#Incrementos
		incordx=52

		for i in range(1,11):
			var=StringVar()
			labelNumeros={}
			labelNumeros["string{0}".format(i)]=Button(self.main,text=i, width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
			var.set(i)
			cordx+=incordx

		""" LETRAS DEL TABLERO 2 """

		#Lista con las letras del tablero
		letras=["A","B","C","D","E","F","G","H","J","K"]

		#Variables
		m=1
		cordx=748
		cordy=140

		#Incrementos
		incm=1
		incordy=40
		for l in letras:
		    tempLetra=letras[m-1]
		    var=StringVar()
		    labelNumeros={}
		    labelNumeros["string{0}".format(l)]=Button(self.main,text=tempLetra,width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
		    var.set(l)
		    m+=incm
		    cordy+=incordy

		""" BOTONES DEL TABLERO 2 """

		#Variables
		cordx=800
		cordy=140

		#Incrementos
		incordx=52
		incordy=40

		#Constantes
		conCordx=800
		for i in range(10):
			for j in range(10):
				boton={}
				boton["{0}".format(i)]=Button(self.main,width=6, height=2,command=lambda i=i, j=j,cordx=cordx,cordy=cordy:self.valTablero([i,j],2,cordx,cordy))
				boton["{0}".format(i)].place(x=cordx,y=cordy)
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		self.main.mainloop()

	def tableroCumputadora(self):
		global nombreJugador1,nombreJugador2,turno
		self.main.state("zoomed")
		"""Nombres del tablero"""
		labelJugador = Label(self.main,text=nombreJugador1)
		labelJugador.place(x=262,y=70)
		labelJugador.config(font=("Courier", 16))

		labelComputadora = Label(self.main,text="Computadora")
		labelComputadora.place(x=1000,y=70)
		labelComputadora.config(font=("Courier", 16))


		botonReiniciar = Button(self.main,text="Reiniciar juego",command=lambda: self.reiniciarJuego()).place(x=0,y=560)



		""" NUMEROS DEL TABLERO 1 """

		cordx=62	#Valor coordenada x
		cordy=100	#Valor coordenada y

		incordx=52	#Incremento de la variable x

		for i in range(1,11):
			var=StringVar()
			labelNumeros={}
			labelNumeros["string{0}".format(i)]=Button(self.main,text=i, width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
			var.set(i)
			cordx+=incordx

		""" LETRAS DEL TABLERO 1"""

		letras=["A","B","C","D","E","F","G","H","J","K"]	#Lista con las letras que se encuentran en el tablero

		m=1			#Posición de la letra en la lista
		cordx=10	#Valor de la coordenada x
		cordy=140	#Valor de la coordenada y

		incordy=40	#Incremento de la coordenada y
		incm=1		#Incremento de la posición de la letra

		for l in letras:
		    tempLetra=letras[m-1]
		    var=StringVar()
		    labelNumeros={}
		    labelNumeros["string{0}".format(l)]=Button(self.main,text=tempLetra,width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
		    var.set(l)
		    m+=incm
		    cordy+=incordy

		""" BOTONES DEL TABLERO 1"""

		cordx=62	#Incremento de la coordenada x
		cordy=140	#Incremento de la coordenada y

		incordy=40	#Incremento de la coordenada y
		incordx=52	#Incremento de la coordenada x

		conCordx=62	#Reinicio del valor de la coordeda x

		for i in range(10):
			for j in range(10):
				boton={}
				boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
				boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
				if matrizMultijugador1[i][j] in {2,4,6}:
					photo=PhotoImage(file="barco.png")
					boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
					boton["boton{0}".format([i,j])].image=photo
				elif matrizMultijugador1[i][j] == 0:
					photo2=PhotoImage(file="agua.png")
					boton["boton{0}".format([i,j])].config(image=photo2,width=46,height=35)
					boton["boton{0}".format([i,j])].image=photo2
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		""" NUMEROS DEL TABLERO 2 """

		cordx = 800	#Valor de la coordenada x
		cordy = 100	#Valor de la coordenada y

		incordx=52	#Incremento de la coordenada x

		for i in range(1,11):
			var=StringVar()
			labelNumeros={}
			labelNumeros["string{0}".format(i)]=Button(self.main,text=i, width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
			var.set(i)
			cordx+=incordx

		""" LETRAS DEL TABLERO 2 """

		letras=["A","B","C","D","E","F","G","H","J","K"]	#Lista con las letras del tablero

		m=1			#Posición de la letra en la lista
		cordx=748	#Valor de la coordenada x
		cordy=140	#Valor de la coordenada y

		incm=1		#Incremento de la posición de la letra en la lista
		incordy=40	#Incremento de la coordenada y
		for l in letras:
		    tempLetra=letras[m-1]
		    var=StringVar()
		    labelNumeros={}
		    labelNumeros["string{0}".format(l)]=Button(self.main,text=tempLetra,width=6,height=2,state=DISABLED).place(x=cordx,y=cordy)
		    var.set(l)
		    m+=incm
		    cordy+=incordy

		""" BOTONES DEL TABLERO 2 """

		#Variables
		cordx=800
		cordy=140

		#Incrementos
		incordx=52
		incordy=40

		#Constantes
		conCordx=800
		for i in range(10):
			for j in range(10):
				boton={}
				boton["{0}".format(i)]=Button(self.main,width=6, height=2,command=lambda i=i, j=j,cordx=cordx,cordy=cordy:self.valTablero([i,j],3,cordx,cordy))
				boton["{0}".format(i)].place(x=cordx,y=cordy)
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		self.main.mainloop()

	def valTablero (self,coordenada,tablero,cordx,cordy):
		global matrizMultijugador1,turno
		if tablero == 1:
			if turno == 1:
				turno = 2
				LabelTurno = Label(self.main,text="Es el turno del jugador 1")
				LabelTurno.place(x=500, y= 20)
				LabelTurno.config(font=("Courier", 16))
				if matrizMultijugador1[coordenada[0]] [coordenada[1]] in {2,4,6}:
					matrizMultijugador1[coordenada[0]] [coordenada[1]]-=1
					for i in range(10):
						for j in range(10):
							if matrizMultijugador1[i][j] in {1,3,5}:
								boton={}
								boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
								boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
								photo = PhotoImage(file="barco.png")
								boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
								boton["boton{0}".format([i,j])].image=photo


					if self.ganarJuego(0):
						self.main.destroy()
						nueva=Toplevel()
						a = ventanaGane(nueva)
						a.gameOver()

				elif matrizMultijugador1[coordenada[0]] [coordenada[1]] == 0:
					matrizMultijugador1[coordenada[0]] [coordenada[1]]-=1
					for i in range(10):
						for j in range(10):
							if matrizMultijugador1[i][j] == -1:
								boton={}
								boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
								boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
								photo = PhotoImage(file="agua.png")
								boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
								boton["boton{0}".format([i,j])].image=photo				
			else:
				botonTurno = Label(self.main,text="No es el turno del jugado 2")
				botonTurno.place(x=500, y= 20)
				botonTurno.config(font=("Courier",15))

		elif tablero == 2:
			if turno == 2:
				turno=1
				LabelTurno = Label(self.main,text="Es el turno del jugador 2")
				LabelTurno.place(x=500, y= 20)
				LabelTurno.config(font=("Courier", 16))
				if matrizMultijugador2[coordenada[0]] [coordenada[1]] in {2,4,6}:
					matrizMultijugador2[coordenada[0]] [coordenada[1]]-=1
					for i in range(10):
						for j in range(10):
							if matrizMultijugador2[i][j] in {1,3,5}:
								boton={}
								boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
								boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
								photo = PhotoImage(file="barco.png")
								boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
								boton["boton{0}".format([i,j])].image=photo

					if self.ganarJuego(0):
						nueva=Toplevel(self.main)
						a = ventanaGane(nueva)
						a.gameOver()		

				elif matrizMultijugador2 [coordenada[0]] [coordenada[1]] == 0:
					matrizMultijugador2[coordenada[0]] [coordenada[1]]-=1
					for i in range(10):
						for j in range(10):
							if matrizMultijugador2[i][j] == -1:
								boton={}
								boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
								boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
								photo = PhotoImage(file="agua.png")
								boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
								boton["boton{0}".format([i,j])].image=photo				
			else:
				botonTurno = Label(self.main,text="No es el turno del jugado 1")
				botonTurno.place(x=500, y= 20)
				botonTurno.config(font=("Courier",15))

		elif tablero == 3:
			if matrizvsComputadora[coordenada[0]] [coordenada[1]] in {2,4,6}:
				matrizvsComputadora[coordenada[0]] [coordenada[1]]-=1
				for i in range(10):
					for j in range(10):
						if matrizvsComputadora[i][j] in {1,3,5}:
							boton={}
							boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
							boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
							photo = PhotoImage(file="barco.png")
							boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
							boton["boton{0}".format([i,j])].image=photo
				self.juegaComputadora()


				if self.ganarJuego(0):
					self.main.destroy()
					nueva=Toplevel()
					a = ventanaGane(nueva)
					a.gameOver()

			elif matrizvsComputadora[coordenada[0]] [coordenada[1]] == 0:
				matrizvsComputadora[coordenada[0]] [coordenada[1]]-=1
				for i in range(10):
					for j in range(10):
						if matrizvsComputadora[i][j] == -1:
							boton={}
							boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
							boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
							photo = PhotoImage(file="agua.png")
							boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
							boton["boton{0}".format([i,j])].image=photo	
				self.juegaComputadora()	

	def juegaComputadora(self):#debe enviar como si fuera un botón a la función validar para que envie las coordenadas y el tablero para luego cambiar la imágen
		global matrizMultijugador1
		matrizMultijugador1[random.randrange(10)][random.randrange(10)]-=1
		cordx=62	#Incremento de la coordenada x
		cordy=140	#Incremento de la coordenada y

		incordy=40	#Incremento de la coordenada y
		incordx=52	#Incremento de la coordenada x

		conCordx=62	#Reinicio del valor de la coordeda x

		for i in range(10):
			for j in range(10):
				if matrizMultijugador1[i][j] in{1,3,5}:
					boton={}
					boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
					boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
					photo = PhotoImage(file="bomba.png")
					boton["boton{0}".format([i,j])].config(image=photo,width=46,height=35)
					boton["boton{0}".format([i,j])].image=photo
				if matrizMultijugador1[i][j] == -1:
					boton={}
					boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2)
					boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)					
					photo2 = PhotoImage(file="splash.png")
					boton["boton{0}".format([i,j])].config(image=photo2,width=46,height=35)
					boton["boton{0}".format([i,j])].image=photo2
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx										


	def ganarJuego(self,matriz):
		if matriz==0:
			for i in range(10):
				for j in range(10):
					print(i)
					if matrizMultijugador1[i][j] in {2,4,6}:
						return False
			return True
		elif matriz == 1:
			for i in matrizMultijugador1:
				for j in matrizMultijugador1:
					if matrizMultijugador1[i][j] in {2,4,6}:
						return False
			return True

		else:
			for i in matrizMultijugador1:
				for j in matrizvsComputadora:
					if matrizvsComputadora[i][j] in {2,4,6}:
						return False
			return True

	def reiniciarJuego(self):
		global matrizMultijugador1,matrizMultijugador2,matrizvsComputadora
		cordx=62
		cordy=140

		#Incrementos
		incordy=40
		incordx=52

		#Constante
		conCordx=62

		for i in range(10):
			for j in range(10):
				boton={}
				boton["boton{0}".format([i,j])]=Button(self.main,width=6,height=2,command=lambda i=i, j=j,cordx=cordx,cordy=cordy:self.valTablero([i,j],1,cordx,cordy))
				boton["boton{0}".format([i,j])].place(x=cordx,y=cordy)
				""" MULTIJUGADOR"""
				if matrizMultijugador1 [i][j] == -1 or matrizMultijugador2[i][j] == -1: #Si es un espacio vacío
					matrizMultijugador1 [i][j] = 0
					matrizMultijugador2 [i][j] = 0

				elif matrizMultijugador1 [i][j] == 1 or matrizMultijugador2[i][j] == 1:#Si es un portaaviones
					matrizMultijugador1 [i][j] = 2
					matrizMultijugador2 [i][j] = 2

				elif matrizMultijugador1 [i] [j] == 3 or matrizMultijugador2[i][j] == 3: #si la matriz es un buque
					matrizMultijugador1 [i][j] = 4
					matrizMultijugador2 [i][j] = 4

				elif matrizMultijugador1 [i][j] == 5 or matrizMultijugador2[i][j] == 5: #si la matriz es una lancha
					matrizMultijugador1 [i][j] = 6
					matrizMultijugador2 [i][j] = 6

				elif matrizvsComputadora [i][j] == -1: #Si es un espacio vacío
					matrizvsComputadora [i][j] = 0

				elif matrizvsComputadora [i][j] == 1:#Si es un portaaviones
					matrizvsComputadora [i][j] = 2

				elif matrizvsComputadora [i] [j] == 3: #si la matriz es un buque
					matrizvsComputadora [i][j] = 4

				elif matrizvsComputadora [i][j] == 5: #si la matriz es una lancha
					matrizvsComputadora [i][j] =6



				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		#Variables
		cordx=800
		cordy=140

		#Incrementos
		incordx=52
		incordy=40

		#Constantes
		conCordx=800
		for i in range(10):
			for j in range(10):
				boton={}
				boton["{0}".format(i)]=Button(self.main,width=6, height=2,command=lambda i=i, j=j,cordx=cordx,cordy=cordy:self.valTablero([i,j],2,cordx,cordy))
				boton["{0}".format(i)].place(x=cordx,y=cordy)
				""" MULTIJUGADOR"""
				if matrizMultijugador1 [i][j] == -1 or matrizMultijugador2 == -1: #Si es un espacio vacío
					matrizMultijugador1 [i][j] = 0
					matrizMultijugador2 [i][j] = 0

				elif matrizMultijugador1 [i][j] == 1 or matrizMultijugador2 == 1:#Si es un portaaviones
					matrizMultijugador1 [i][j] = 2
					matrizMultijugador2 [i][j] = 2

				elif matrizMultijugador1 [i] [j] == 3 or matrizMultijugador2 == 3: #si la matriz es un buque
					matrizMultijugador1 [i][j] = 4
					matrizMultijugador2 [i][j] = 4

				elif matrizMultijugador1 [i][j] == 5 or matrizMultijugador2 == 5: #si la matriz es una lancha
					matrizMultijugador1 [i][j] = 6
					matrizMultijugador2 [i][j] = 6

					"""VS COMPUTADORA"""
				elif matrizvsComputadora [i][j] == -1: #Si es un espacio vacío
					matrizvsComputadora [i][j] = 0

				elif matrizvsComputadora [i][j] == 1:#Si es un portaaviones
					matrizvsComputadora [i][j] = 2

				elif matrizvsComputadora [i] [j] == 3: #si la matriz es un buque
					matrizvsComputadora [i][j] = 4

				elif matrizvsComputadora [i][j] == 5: #si la matriz es una lancha
					matrizvsComputadora [i][j] =6

				cordx+=incordx
			cordy+=incordy
			cordx=conCordx





class ventanaGane:
	def __init__(self, main):
		self.main=main
		w, h = self.main.winfo_screenwidth(), self.main.winfo_screenheight()
		self.main.state("zoomed")

	def gameOver(self):
		photo = PhotoImage(file="GameOver.png")
		background_label = Label(self.main, image=photo)
		background_label.place(x=0, y=0, relwidth=1, relheight=1)
		background_label.image = photo		

		#BOTONES DE REINICIO Y QUITAR JUEGO
		photo = PhotoImage(file="reiniciar.png")
		reiniciar = Button (self.main, image=photo, command=lambda:self.reiniciarJuego()).place(x=600,y=600)

		photo2 = PhotoImage(file="textoGameOver.png")
		juegoterminado= Label(self.main,image=photo2).place(x=400,y=300)

		self.main.mainloop()

	def reiniciarJuego(self):
		global ambientacion,nombreJugador1,nombreJugador2,matrizMultijugador1,matrizMultijugador2, matrizvsComputadora
		ambientacion   = 0
		nombreJugador1 = "Jugador 1"
		nombreJugador2 = "Jugador 2"

		"""MATRICES DE LOS TABLEROS"""
		matrizMultijugador1  = [[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0]]

		matrizMultijugador2  = [[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0]]

		matrizvsComputadora  = [[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0,0,0]]

		"""EMBARCACIONES"""
		global portaavionesJugador1,portaavionesJugador2,buqueJugador1,buqueJugador2,lanchaJugador1,labelJugador2
			#Embarcaciones Jugador 1
		portaavionesJugador1 = 2
		buqueJugador1 = 3
		lanchaJugador1 = 4

			#Embarcaciones Jugador 2
		portaavionesJugador2 = 2
		buqueJugador2 = 3
		lanchaJugador2 = 4

		global portaavionesVsComputadora,buqueVsComputadora,lanchaVsComputadora
			#Embarcaciones vs Computadora
		portaavionesVsComputadora= 2
		buqueVsComputadora = 3
		lanchaVsComputadora = 4

		self.main.destroy()

class menuPrincipal:
	def __init__(self,main):
		self.main=main
		self.main.geometry("640x360")

	def app(self):
		self.main.resizable(width=False, height=False)
		photo = PhotoImage(file="pantalla_principal.png")
		background_label = Label(self.main, image=photo)
		background_label.place(x=0, y=0, relwidth=1, relheight=1)
		background_label.image = photo	

		""" Tipo de juego """
		labelTipoJuego = Label(self.main,text="Tipo de juego",bg="white").place(x=20,y=0)
		valTipoJuego = IntVar()

		normal = Radiobutton(self.main,text="Normal",value = 0,variable=valTipoJuego,bg="white").place(x=20,y=20)
		contra_disparos = Radiobutton(self.main,text="Contra Disparos",value=1, variable=valTipoJuego,bg="white").place(x=20,y=40)

		""" MODO DE JUEGO """
		labelModoJuego = Label(self.main,text="Modo de juego",bg="white").place(x=520, y=0)
		valModoJuego = IntVar()#Se guarda valores del radiobutton de Modo de juego
		

		multijugador = Radiobutton(self.main,text="Multijugador",value=0,variable=valModoJuego, bg="white").place(x=520, y=20)
		computadora  = Radiobutton(self.main,text="VS computadora",value=1,variable=valModoJuego, bg="white").place(x=520, y=40)

		#SELECCIONAR NOMBRE Y UBICACIÓN DE LOS BARCOS
		selec_nombre = Button(self.main,text="Seleccionar nombre",bg="white",command=lambda:self.selecNombre()).place(x=20,y=220) 	
		selec_ubicacion = Button (self.main,text="Seleccionar ubicación de los barcos",bg="white",command=lambda:self.selecUbicacion(valModoJuego.get())).place(x=20,y=245) 	


		"""SELECCIONAR AMBIENTE"""
		labelSelecAmbiente = Label(self.main,text="Seleccionar Ambiente").place(x=510,y=150)
		valSelecAmbiente = IntVar()

		cordx=510
		pacificoCentral = Radiobutton(self.main,variable=valSelecAmbiente,value=0,text="Pacífico Central",bg="white").place(x=cordx,y=175)
		piratasDelCaribe = Radiobutton(self.main,variable=valSelecAmbiente,value=1, text= "Piratas del Caribe",bg="white").place(x=cordx,y=200)
		regionPolar = Radiobutton(self.main,variable=valSelecAmbiente,value=2, text= "Región Polar",bg="white").place(x=cordx,y=225)
		vikingo = Radiobutton(self.main,variable=valSelecAmbiente,value=3, text= "Vikingos",bg="white").place(x=cordx,y=250)

		"""Iniciar juego"""
		iniciar_juego = Button(self.main,text="Iniciar",bg="white",width=15,height=2,command=lambda:self.iniciarJuego(valModoJuego.get(),valSelecAmbiente.get())).place(x=270, y=300)


		self.main.mainloop()

	def selecUbicacion(self,modoJuego):
		nueva = Toplevel(self.main)

		if modoJuego == 0:
			global nombreJugador1,nombreJugador2
			nueva.geometry("720x400")
			nueva.title("Seleccionar ubicación de los barcos")

			"""NOMBRES DEL TABLERO"""
			labelJugador1 = Label(nueva,text=nombreJugador1).place(x=160,y=20)
			labelJugador2 = Label(nueva,text=nombreJugador2).place(x=520,y=20)

			labelSelecUbicacion = Label(nueva,text="Seleccionar ubicación de los barcos").place(x=265,y=10)

			"""EMBARCACIOINES"""

				#Embarcaciones Jugador 1
			embarcaciones1=IntVar()
			portaaviones= Radiobutton(nueva,text="Portaaviones",value = 0,variable=embarcaciones1).place(x=0,y=370)
			buques=Radiobutton(nueva,text="Buques",value = 1,variable=embarcaciones1).place(x=100,y=370)
			lanchas=Radiobutton(nueva,text="Lanchas",value = 2,variable=embarcaciones1).place(x=170,y=370)

				#Posición de las embarcaciones del jugador 1 
			posembarcacion1=IntVar()
			horizontal=Radiobutton(nueva,text="Horizontal",value = 0,variable=posembarcacion1).place(x=0,y=330)
			vertical=Radiobutton(nueva,text="Vertical",value = 1,variable=posembarcacion1).place(x=80,y=330)

				#Embarcaciones Jugador 2
			embarcaciones2=IntVar()
			portaaviones= Radiobutton(nueva,text="Portaaviones",value = 0,variable=embarcaciones2).place(x=480,y=370)
			buques=Radiobutton(nueva,text="Buques",value = 1,variable=embarcaciones2).place(x=580,y=370)
			lanchas=Radiobutton(nueva,text="Lanchas",value = 2,variable=embarcaciones2).place(x=650,y=370)

				#Posición de las embarcaciones del jugador 2
			posembarcacion2=IntVar()
			horizontal=Radiobutton(nueva,text="Horizontal",value = 0,variable=posembarcacion2).place(x=570,y=330)
			vertical=Radiobutton(nueva,text="Vertical",value = 1,variable=posembarcacion2).place(x=650,y=330)			

			""" NUMEROS DEL TABLERO 1 """

			cordx=40	#Coordenada x
			cordy=50	#Coordenada y

			incordx=30	#incremento de la coordenada x

			for i in range(1,11):
				var=StringVar()
				labelNumeros={}
				labelNumeros["string{0}".format(i)]=Button(nueva,text=i, width=3,state=DISABLED).place(x=cordx,y=cordy)
				var.set(i)
				cordx+=incordx

			""" LETRAS DEL TABLERO 1"""

			letras=["A","B","C","D","E","F","G","H","J","K"] #Lista con las letras que se encuentran en el tablero

				
			m=1 		#Posición de letras
			cordx=10	#Coordenada x
			cordy=75	#Coordenada y

				
			incordy=25 #Incremento de la coordenada y
			incm=1     #Incremento de la posición de la lista de las letras

			for l in letras:
			    tempLetra=letras[m-1]
			    var=StringVar()
			    labelNumeros={}
			    labelNumeros["string{0}".format(l)]=Button(nueva,text=tempLetra,width=3,state=DISABLED).place(x=cordx,y=cordy)
			    var.set(l)
			    m+=incm
			    cordy+=incordy

			""" BOTONES DEL TABLERO 1"""

			cordx=40 #
			cordy=75 #Coordena
				
			incordy=25 #Incremento de la coordenadna y
			incordx=30 #Incremento de la coordenada x
				
			conCordx=40 #Se reinicia el valor de la coordenada x
			for i in range(10):
				for j in range(10):
					boton={}
					boton["{0}".format([i,j])]=Button(nueva,width=3,command=lambda i=i, j=j:self.modificarMatriz([i,j],1,embarcaciones1.get(),posembarcacion1.get(),nueva))
					boton["{0}".format([i,j])].place(x=cordx,y=cordy)
					cordx+=incordx
				cordy+=incordy
				cordx=conCordx

			""" NUMEROS DEL TABLERO 2 """

			cordx = 400 #Coordenadna x
			cordy = 50	#coordenadna y

			incordx=30 #Incrementos de pixeles de la coordenada x

			for i in range(1,11):
				var=StringVar()
				labelNumeros={}
				labelNumeros["string{0}".format(i)]=Button(nueva,text=i, width=3,state=DISABLED).place(x=cordx,y=cordy)
				var.set(i)
				cordx+=incordx

			""" LETRAS DEL TABLERO 2 """

			letras=["A","B","C","D","E","F","G","H","J","K"] #Lista con las letras del tablero

				
			m=1
			cordx=370 #Coordenada X
			cordy=75  #CoordenandaY

				
			incm=1 
			incordy=25 #Cantidades de pixeles que se le incrementa a la coordenada y
			for l in letras:
			    tempLetra=letras[m-1]
			    var=StringVar()
			    labelNumeros={}
			    labelNumeros["string{0}".format(l)]=Button(nueva,text=tempLetra,width=3,state=DISABLED).place(x=cordx,y=cordy)
			    var.set(l)
			    m+=incm
			    cordy+=incordy


			""" BOTONES DEL TABLERO 2 """

				#Variables
			cordx=400
			cordy=75

				#Incrementos
			incordx=30
			incordy=25

				#Constantes
			conCordx=400
			for i in range(10):
				for j in range(10):
					boton={}
					boton["string{0}".format(i)]=Button(nueva,width=3,command=lambda i=i, j=j:self.modificarMatriz([i,j],2,embarcaciones2.get(),posembarcacion2.get(),nueva)).place(x=cordx,y=cordy)
					cordx+=incordx
				cordy+=incordy
				cordx=conCordx



			self.main.mainloop()			

		else:#Se necesita arreglar la forma de seleccionar barcos en vs computadora
			nueva.geometry("360x400")
			nueva.title("Seleccionar ubicación de los barcos")

			"""NOMBRES DEL TABLERO"""
			labelJugador1 = Label(nueva,text=nombreJugador1).place(x=160,y=20)

			"""EMBARCACIOINES"""

				#Embarcaciones Jugador 1
			embarcaciones1=IntVar()
			portaaviones= Radiobutton(nueva,text="Portaaviones",value = 0,variable=embarcaciones1).place(x=0,y=370)
			buques=Radiobutton(nueva,text="Buques",value = 1,variable=embarcaciones1).place(x=100,y=370)
			lanchas=Radiobutton(nueva,text="Lanchas",value = 2,variable=embarcaciones1).place(x=170,y=370)

				#Posición de las embarcaciones del jugador 1 
			posembarcacion1=IntVar()
			horizontal=Radiobutton(nueva,text="Horizontal",value = 0,variable=posembarcacion1).place(x=0,y=330)
			vertical=Radiobutton(nueva,text="Vertical",value = 1,variable=posembarcacion1).place(x=80,y=330)		

			""" NUMEROS DEL TABLERO 1 """

			cordx=40	#Coordenada x
			cordy=50	#Coordenada y

			incordx=30	#incremento de la coordenada x

			for i in range(1,11):
				var=StringVar()
				labelNumeros={}
				labelNumeros["string{0}".format(i)]=Button(nueva,text=i, width=3,state=DISABLED).place(x=cordx,y=cordy)
				var.set(i)
				cordx+=incordx

			""" LETRAS DEL TABLERO 1"""

			letras=["A","B","C","D","E","F","G","H","J","K"] #Lista con las letras que se encuentran en el tablero

				
			m=1 		#Posición de letras
			cordx=10	#Coordenada x
			cordy=75	#Coordenada y

				
			incordy=25 #Incremento de la coordenada y
			incm=1     #Incremento de la posición de la lista de las letras

			for l in letras:
			    tempLetra=letras[m-1]
			    var=StringVar()
			    labelNumeros={}
			    labelNumeros["string{0}".format(l)]=Button(nueva,text=tempLetra,width=3,state=DISABLED).place(x=cordx,y=cordy)
			    var.set(l)
			    m+=incm
			    cordy+=incordy

			""" BOTONES DEL TABLERO 1"""

			cordx=40 #
			cordy=75 #Coordena
				
			incordy=25 #Incremento de la coordenadna y
			incordx=30 #Incremento de la coordenada x
				
			conCordx=40 #Se reinicia el valor de la coordenada x
			for i in range(10):
				for j in range(10):
					boton={}
					boton["{0}".format([i,j])]=Button(nueva,width=3,command=lambda i=i, j=j:self.modificarMatriz([i,j],1,embarcaciones1.get(),posembarcacion1.get(),nueva))
					boton["{0}".format([i,j])].place(x=cordx,y=cordy)
					cordx+=incordx
				cordy+=incordy
				cordx=conCordx

	def modificarMatriz(self,coordenada,tablero,embarcacion,posembarcacion,ventana):
		global matrizMultijugador1,matrizMultijugador2 #MATRICES DE MULTIJUGADOR
		global portaavionesJugador1,portaavionesJugador2,buqueJugador1,buqueJugador2,lanchaJugador1,lanchaJugador2 #EMBARCACIONES DE MULTIJUGADOR
		global portaavionesVsComputadora,buqueVsComputadora,lanchaVsComputadora #EMBARCACIONES DE VS COMPUTADORA

		#tablero (0 = Vs computadora, 1 = Multijuador 1, 2 = Multijugador 2)
		#embarcacion (0 = portaavriones {cuatro casillas}, 1 = Buque {tres casillas}, 2 = Lanchas {una casilla})

		if tablero == 1: #Tablero del jugador 1
			if embarcacion == 0 and portaavionesJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):							
							portaavionesJugador1-=1
							for i in range(4):								
								matrizMultijugador1 [coordenada[0]][coordenada[1]+i] = 2
								self.ActualizarTablero(ventana)
						else: 
							print("No se puede colocar la embarcacion en esa posición")							
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):							
							portaavionesJugador1-=1
							for i in range(4):								
								matrizMultijugador1 [coordenada[0]+i][coordenada[1]] = 2
								self.ActualizarTablero(ventana)
						else: 
							print("No se puede colocar la embarcacion en esa posición")							
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")				

			elif embarcacion == 1 and buqueJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
							buqueJugador1-=1
							for i in range(3):								
								matrizMultijugador1 [coordenada[0]][coordenada[1]+i] = 4
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
							buqueJugador1-=1
							for i in range(3):								
								matrizMultijugador1 [coordenada[0]+i][coordenada[1]] = 4
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")				

			elif embarcacion == 2 and lanchaJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
						lanchaJugador1 -=1						
						matrizMultijugador1 [coordenada[0]][coordenada[1]] = 6
						self.ActualizarTablero(ventana)
					else:	
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
						lanchaJugador1 -=1						
						matrizMultijugador1 [coordenada[0]][coordenada[1]] = 6
						self.ActualizarTablero(ventana)
					else:	
						print("No se puede colocar la embarcacion en esa posición")				

		elif tablero == 2: #TABLERO DEL JUGADOR 2
			if embarcacion == 0 and portaavionesJugador2 >0:
				if posembarcacion == 0: #Si la posición es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion): 
							portaavionesJugador2-=1
							for i in range(4):								
								matrizMultijugador2 [coordenada[0]][coordenada[1]+i] = 2
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else:#Si la posición es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion): 
							portaavionesJugador2-=1
							for i in range(4):								
								matrizMultijugador2 [coordenada[0]+i][coordenada[1]] = 2
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")				

			elif embarcacion == 1 and buqueJugador2 >0:
				if posembarcacion == 0: #Si la posición es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
							buqueJugador2-=1
							for i in range(3):								
								matrizMultijugador2 [coordenada[0]][coordenada[1]+i] = 4
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
							buqueJugador2-=1
							for i in range(3):								
								matrizMultijugador2 [coordenada[0]+i][coordenada[1]] = 4
								self.ActualizarTablero(ventana)
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

			elif embarcacion == 2 and lanchaJugador2 >0:
				if posembarcacion == 0: #Si la posición es horizontal
					if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
						lanchaJugador2 -=1						
						matrizMultijugador2 [coordenada[0]][coordenada[1]] = 6
						self.ActualizarTablero(ventana)
					else:
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición es vertical
					if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
						lanchaJugador2 -=1						
						matrizMultijugador2 [coordenada[0]][coordenada[1]] = 6
						self.ActualizarTablero(ventana)	
					else:
						print("No se puede colocar la embarcacion en esa posición")					

		else:
			if embarcacion == 0 and portaavionesJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):							
							portaavionesVsComputadora-=1
							for i in range(4):								
								matrizMultijugador1 [coordenada[0]][coordenada[1]+i] = 2
						else: 
							print("No se puede colocar la embarcacion en esa posición")							
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):							
							portaavionesJugador1-=1
							for i in range(4):								
								matrizMultijugador1[coordenada[0]+i][coordenada[1]] = 2
						else: 
							print("No se puede colocar la embarcacion en esa posición")							
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")				

			elif embarcacion == 1 and buqueJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					try:
						if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
							buqueJugador1-=1
							for i in range(3):								
								matrizMultijugador1 [coordenada[0]][coordenada[1]+i] = 4
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					try:
						if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
							buqueJugador1-=1
							for i in range(3):								
								matrizMultijugador1 [coordenada[0]+i][coordenada[1]] = 4
						else:
							print("No se puede colocar la embarcacion en esa posición")
					except IndexError :
						print("No se puede colocar la embarcacion en esa posición")				

			elif embarcacion == 2 and lanchaJugador1 >0:
				if posembarcacion == 0: #Si la posición de la embarcación es horizontal
					if self.posicionValida(tablero,coordenada[0],coordenada[1]-1,embarcacion,posembarcacion):
						lanchaJugador1 -=1						
						matrizMultijugador1 [coordenada[0]][coordenada[1]] = 6
					else:	
						print("No se puede colocar la embarcacion en esa posición")

				else: #Si la posición de la embarcación es vertical
					if self.posicionValida(tablero,coordenada[0]-1,coordenada[1],embarcacion,posembarcacion):
						lanchaJugador1 -=1						
						matrizMultijugador1 [coordenada[0]][coordenada[1]] = 6
					else:	
						print("No se puede colocar la embarcacion en esa posición")				 #CAMBIAR TODO LO QUE DICE VS COMPUTADORA, EL JUGADOR 1 REEMPLAZARA  LA PERSONAS, LA COMPUTADORA SERÁ UNA FUNCIÓN APARTE

	def ActualizarTablero (self,ventana):
		global matrizMultijugador1,matrizMultijugador2 #MATRICES DE MULTIJUGADOR
			#Variables
		cordx=40
		cordy=75

			#Incrementos
		incordy=25
		incordx=30

			#Constante
		conCordx=40
		for i in range(10):
			for j in range(10):
				boton={}
				if matrizMultijugador1[i][j] != 0: 
					boton["{0}".format([i,j])]=Button(ventana,width=3)
					boton["{0}".format([i,j])].place(x=cordx,y=cordy)
					boton["{0}".format([i,j])].config(bg="red")
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx

		""" BOTONES DEL TABLERO 2 """

			#Variables
		cordx=400
		cordy=75

			#Incrementos
		incordx=30
		incordy=25

			#Constantes
		conCordx=400
		for i in range(10):
			for j in range(10):
				boton={}
				if matrizMultijugador2 [i][j] != 0: 					
					boton["string{0}".format(i)]=Button(ventana,width=3)
					boton["string{0}".format(i)].place(x=cordx,y=cordy)
					boton["string{0}".format(i)].config(bg="blue")					
				cordx+=incordx
			cordy+=incordy
			cordx=conCordx			

	def posicionValida(self,matriz,x,y,embarcacion,posicion):
		if posicion==0: # Si la posicion es horizontal
			if matriz == 1: # Multijugador 1
				if embarcacion == 0:
					for i in range(0,5):
						if matrizMultijugador1 [x][y+i] != 0 or matrizMultijugador1 [x-1][y+i] !=0 or matrizMultijugador1[x+1][y+i] !=0:
							return False
					return True
				elif embarcacion == 1:
					for i in range(0,4):
						if matrizMultijugador1 [x][y+i] != 0 or matrizMultijugador1 [x-1][y+i] !=0 or matrizMultijugador1[x+1][y+i] !=0:
							return False
					return True	
				elif embarcacion == 2:
					try:
						for i in range(0,2):
							if matrizMultijugador1 [x][y+i] != 0 or matrizMultijugador1 [x-1][y+i] !=0 or matrizMultijugador1[x+1][y+i] !=0:
								return False
						return True		
					except IndexError:
						for i in range(0,2):
							if matrizMultijugador1 [x][y+i] != 0 or matrizMultijugador1 [x-1][y+i] !=0:
								return False
						return True							


			elif matriz == 2: # Multijugador 2
				if embarcacion == 0:
					for i in range(0,5):
						if matrizMultijugador2 [x][y+i] != 0 or matrizMultijugador2 [x-1][y+i] !=0 or matrizMultijugador2[x+1][y+i] !=0:
							return False
					return True
				elif embarcacion == 1:
					for i in range(0,4):
						if matrizMultijugador2 [x][y+i] != 0 or matrizMultijugador2 [x-1][y+i] !=0 or matrizMultijugador2[x+1][y+i] !=0:
							return False
					return True	
				elif embarcacion == 2:
					for i in range(0,2):
						if matrizMultijugador2 [x][y+i] != 0 or matrizMultijugador2 [x-1][y+i] !=0 or matrizMultijugador2[x+1][y+i] !=0:
							return False
					return True							

		else: #Si la posición es vertical
			if matriz == 1: # Multijugador 1
				if embarcacion == 0:
					for i in range(0,5):
						if matrizMultijugador1 [x+i][y] != 0 or matrizMultijugador1 [x+i][y-i] !=0 or matrizMultijugador1[x+i][y+1] !=0:
							return False
					return True
				elif embarcacion == 1:
					for i in range(0,4):
						if matrizMultijugador1 [x+i][y] != 0 or matrizMultijugador1 [x+i][y-1] !=0 or matrizMultijugador1[x+i][y+1] !=0:
							return False
					return True	
				elif embarcacion == 2:
					try:
						for i in range(0,2):
							if matrizMultijugador1 [x+i][y] != 0 or matrizMultijugador1 [x+i][y-1] !=0 or matrizMultijugador1[x+i][y+1] !=0:
								return False
						return True
					except IndexError:
						for i in range(0,2):
							if matrizMultijugador1 [x+i][y] != 0 or matrizMultijugador1 [x+i][y-1] !=0:
								return False
						return True						


			elif matriz == 2: # Multijugador 2
				if embarcacion == 0:
					for i in range(0,5):
						if matrizMultijugador2 [x+i][y] != 0 or matrizMultijugador2 [x+i][y-1] !=0 or matrizMultijugador2[x+i][y+1] !=0:
							return False
					return True
				elif embarcacion == 1:
					for i in range(0,4):
						if matrizMultijugador2 [x+i][y] != 0 or matrizMultijugador2 [x+i][y-1] !=0 or matrizMultijugador2[x+i][y+1] !=0:
							return False
					return True	
				elif embarcacion == 2:
					try:
						for i in range(0,2):
							if matrizMultijugador2 [x+i][y] != 0 or matrizMultijugador2 [x+i][y-1] !=0 or matrizMultijugador2[x+i][y+1] !=0:
								return False
						return True							
					except IndexError:
						for i in range(0,2):
							if matrizMultijugador2 [x+i][y] != 0 or matrizMultijugador2 [x+i][y-1] !=0:
								return False
						return True							

	def selecNombre(self):
		nueva=Toplevel(self.main)

		valJugador1=StringVar()
		valJugador2=StringVar()

		labelJugador1 = Label(nueva,text="Jugador 1").pack()
		jugador1 = Entry(nueva, textvariable=valJugador1, bg="white").pack()

		labelJugador2 = Label(nueva,text="Jugador 2").pack()
		jugador2 = Entry(nueva,textvariable=valJugador2, bg="white").pack()

		listo=Button(nueva, text="Listo",command=lambda:self.setNombre(valJugador1.get(),valJugador2.get(),nueva)).pack()

	def setNombre(self,jugador1,jugador2,ventana):	
		global nombreJugador1,nombreJugador2
		nombreJugador1=jugador1
		nombreJugador2=jugador2
		ventana.destroy()

	def iniciarJuego(self,modoJuego,selecAmbiente):
		global ambientacion
		ambientacion = selecAmbiente
		nueva=Toplevel(self.main)
		a = Ventana(nueva)
		a.ambiente()
		if modoJuego == 0:
			a.tableroMultijugador()
		else:
			a.tableroCumputadora()
			a.juegaComputadora()

ventana = Tk()
a=menuPrincipal(ventana)
a.app()
