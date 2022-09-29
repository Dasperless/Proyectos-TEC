from tkinter import  *
from tkinter import messagebox
import random
import time

contador_minas = 0
matriz_temp = []
botones = []
personalizado = []


#E: Una ventana (Tk())
#S: El frame, el tamaño de la ventana, el titulo y el icono que se utilizará en todos las ventanas del juegi
#R: "master" debe ser una ventana (Tk())
def preferencias_ventana(master):
	frame = Frame(master).grid(row = 1, column = 0)
	master.attributes("-fullscreen",True)
	master.title("Busca Minas")
	master.iconbitmap("Texturas\Logo.ico")
	return frame

#E: Una ventana (Tk())
#S: La ventana principal del videojuego
#R: La entrada debe ser una ventana (Tk())
def ventana_principal(master,modo_juego):
	global personalizado,matriz_temp
	if personalizado !=[]:
		modo_juego =cuadricula(len(matriz_temp))
	frame = preferencias_ventana(master)
	img_inicio = PhotoImage(file = "Texturas\Img_fondo.png")
	fondo = Label(frame, image = img_inicio).place(x = -2, y = -2)
	btn_opciones = Button(frame, text='Opciones',font = ("Arial",25), width = 15,bg = "#FFFFFF", command = lambda:opciones(master)).place(x = 150, y = 360)
	btn_ayuda = Button(frame, text='Ayuda',font = ("Arial",25), width = 15,bg = "#FFFFFF", command = lambda:ayuda(master,modo_juego)).place(x = 150, y = 440)
	btn_about = Button(frame, text='Acerca de',font = ("Arial",25), width = 15,bg = "#FFFFFF", command = lambda:acerca_de(master,modo_juego)).place(x = 150, y = 520)
	btn_salir = Button(frame, text='Salir',font = ("Arial",25), width = 15,bg = "#FFFFFF", command = lambda:master.destroy()).place(x = 150, y = 600)
	btn_jugar = Button(frame, text='Jugar',font = ("Arial",25), width = 15,bg = "#FFFFFF", command = lambda:jugar(master,modo_juego)).place(x = 1000, y = 600)
	master.mainloop()

#E: Una ventana y el modo de juego(un número).
#S: la ventana de ayuda del juego
#R: Master debe ser una ventana y modo de juego debe ser un número del 1 al 3
def ayuda(master,modo_juego):
	frame = preferencias_ventana(master)
	img_fondo = PhotoImage(file = "Texturas\Fondo.png")
	fondo = Label(frame, image = img_fondo).place(x = -2, y = -2)
	img_atras = PhotoImage(file = "Texturas\Left-arrow.png")
	btn_atras = Button(frame, image = img_atras,bg = "#FFFFFF", command = lambda:ventana_principal(master,modo_juego)).place(x = 0, y = 0)
	texto =""" 
	Buscaminas - reglas
	El juego consiste en despejar todas las casillas de una pantalla que no oculten una mina.	

	Algunas casillas tienen un número, este número indica las minas que son en todas las casillas circundantes. Así, si una casilla tiene \n	el número 3, significa que de las ocho casillas que hay alrededor (si no es en una esquina o borde) hay 3 con minas y 5 sin minas.\n	Si se descubre una casilla sin número indica que ninguna de las casillas vecinas tiene mina y estas se descubren automáticamente.	

	Si se descubre una casilla con una mina se pierde la partida.	

	Se puede poner una marca en las casillas que el jugador piensa que hay minas para ayudar a descubrir la que están cerca.	
	"""
	instrucciones = Text(master, height=45, width=150)
	instrucciones.place(x=100,y=10)
	instrucciones.insert(END, texto)
	img_instrucciones=PhotoImage(file = "Texturas\gane.png")
	lbl_instrucciones_1=Label(frame, image = img_instrucciones).place(x = 600, y = 240)
	
	master.mainloop()

#E: Ventana (TK()) y dos números.
#S: Muestra lo que está en las casillas de la cuadrícula.
#R: master debe ser una ventana, i debe ser entero positivo, j debe ser entero positivo.
def mostrar(master,i,j):
	global botones,matriz_temp
	if i == len(matriz_temp) :
		return
	elif i == len(matriz_temp) and j == len(matriz_temp):
		botones[i][j]["state"]="disabled"
		if matriz_temp[i][j]==0:
			botones[i][j]["text"]=" "

		elif matriz_temp[i][j]==10:
			botones[i][j]["text"]="✹"
			botones[i][j]["bg"]="red"

		else:
			botones[i][j]["text"]=str(matriz_temp[i][j])
		
	elif j == len(matriz_temp):
		return mostrar(master,i+1,0)
	else:
		botones[i][j]["state"]="disabled"
		if matriz_temp[i][j]==0:
			botones[i][j]["text"]=" "

		elif matriz_temp[i][j]==10:			
			botones[i][j]["text"]="✹"
			botones[i][j]["bg"]="red"

		else:
			botones[i][j]["text"]=str(matriz_temp[i][j])
		return mostrar(master,i,j+1)

#E: Una ventana, y un número.
#S: La ventana de acerca de.
#R: master debe ser una ventana, modo de juego un número entre 1 y 3.
def acerca_de(master,modo_juego):
	frame = preferencias_ventana(master)
	img_fondo = PhotoImage(file = "Texturas\Fondo.png")
	fondo = Label(frame, image = img_fondo).place(x = -2, y = -2)
	img_atras = PhotoImage(file = "Texturas\Left-arrow.png")
	btn_atras = Button(frame, image = img_atras,bg = "#FFFFFF", command = lambda:ventana_principal(master,modo_juego)).place(x = 0, y = 0)
	texto =""" 
	Buscaminas(Minesweeper) 
	Versión 3.6.9 
	©2018 Adrián Darío Vargas Montoya.Todos 
los derechos reservados.
Este archivo está bajo la licencia Creative 
Commons.

Atribución 
CC BY

	"""
	acerca = Text(master, height=20, width=50)
	acerca.place(x=450,y=250)
	acerca.insert(END, texto)
	img_instrucciones=PhotoImage(file = "Texturas\header.png")
	lbl_instrucciones_1=Label(frame, image = img_instrucciones,bg="white").place(x = 385, y = 178)
	
	master.mainloop()

#E: Una ventana (Tk())
#S: La ventana de opciones del juego
#R: La entrada debe ser una ventana (Tk())
def opciones(master):
	frame = preferencias_ventana(master)
	img_fondo = PhotoImage(file = "Texturas\Fondo.png")
	fondo = Label(frame, image = img_fondo).place(x = -2, y = -2)
	lbl_fondo = Label(frame, width = 55, height = 15).place(x = 50, y = 60)
	lbl_dificultad = Label(frame, text = "Dificultad", width = 20, font = ("Arial", 25)).place(x = 50, y = 60)

	v_dificultad = IntVar()
	Radiobutton (master, text = "Dificil", variable = v_dificultad, font = ("Arial", 15), value = 3).place (x = 170, y = 160)
	Radiobutton (master, text = "Medio", variable = v_dificultad, font = ("Arial", 15), value = 2).place (x = 170, y = 200)
	Radiobutton (master, text = "Fácil", variable = v_dificultad, font = ("Arial", 15), value = 1).place (x = 170, y = 240)
	v_dificultad.set(1)

	lbl_cargar = Label(master, text = "Cargar juego personalizado", font = ("Arial", 20)).place(x = 545, y = 300)

	personalizar = Button (master, text = "Personalizar juego", font = ("Arial", 30), command = lambda: personalizar_juego(master,v_dificultad.get()))
	personalizar.place(x = 900, y = 60)

	scrollbar = Scrollbar(master)
	scrollbar.place(x = 1254, y = 350, relheight = 0.435)
	cuadriculas = Listbox(master, font=('Arial',20), width = 80, yscrollcommand = scrollbar.set)
	lista_cuadriculas = crear_lista("Cuadriculas\lista_cuadriculas.txt")
	cuadriculas.insert(END,*lista_cuadriculas)
	cuadriculas.place(x = 50, y = 350 )
	seleccionar =Button (master, text = "Seleccionar",font = ("Arial", 20),command = lambda:seleccionar_cuadricula(cuadriculas.curselection(),lista_cuadriculas)).place(x = 50 , y = 700)

	img_atras = PhotoImage(file = "Texturas\Left-arrow.png")
	btn_atras = Button(frame, image = img_atras,bg = "#FFFFFF", command = lambda:ventana_principal(master,v_dificultad.get() )).place(x = 0, y = 0)
	scrollbar.config( command = cuadriculas.yview )

	master.mainloop()

#E: Una tupla y una lista.
#S: Selecciona una matriz que se encuentra en un txt.
#R: pos debe ser una tupla con un número entero, y lista debe contener los nombres de los txt guardados.
def seleccionar_cuadricula(pos,lista):
	global matriz_temp,personalizado
	nombre = lista[pos[0]][0]
	txt = open("Cuadriculas\\" + nombre + ".txt","r")
	matriz = txt.read()
	matriz_temp = minas_colindantes(eval(matriz),0,0) 
	personalizado = matriz_temp
	txt.close()

	return messagebox.showinfo("Cuadricula seleccionada", "Has seleccionado: "+nombre)

#E: El nombre del archivo (Un string).
#S: Una lista con los elementos de un archivo txt.
#R: archivo debe ser un string.
def crear_lista(archivo):
	txt = open(archivo,"r")
	contenido = txt.read()
	lista = contenido.split("\n")
	resultado = recortar(lista)
	return( limpiar_lista(resultado))

#E: Una lista.
#S: Separa los strings por "," y los pone en una lista.
#R: lista debe ser una lista con strings.
def recortar(lista):
	if lista == []:
		return []
	else:
		return [lista[0].split(",")] + recortar(lista[1:])

#E: Una lista.
#S: Limpia la lista de listas con string vacíos.
#R:	lista debe ser una lista con strings.
def limpiar_lista(lista):
	if lista == []:
		return []
	elif lista[0] == [""]:
		return limpiar_lista(lista[1:])
	else:
		return [lista[0]] + limpiar_lista(lista[1:])

#E: Una ventana, un número
#S: La ventna de personalizar el juego
#R: master debe ser una ventana Tk(), y modo de juego debe ser un número del 1 al 3
def personalizar_juego(master,modo_juego):
	global contador_minas,matriz_temp
	contador_minas = cant_minas(modo_juego)
	frame 		= 	preferencias_ventana(master)
	img_fondo 	= 	PhotoImage(file = "Texturas\Fondo.png")
	fondo 		= 	Label(frame, image = img_fondo).place(x = -2, y = -2)
	img_atras 	= 	PhotoImage(file = "Texturas\Left-arrow.png")
	btn_atras 	=	Button(frame, image = img_atras,bg = "#FFFFFF", command = lambda:opciones(master)).place(x = 0, y = 0)
	nombre 		= 	StringVar()

	tit_entry	=	Label  (frame, text = "Nombre", font = ("Arial",14)).place(x = 420, y = 570)
	inp_nombre	=	Entry  (frame, textvariable = nombre, width = 40).place(x = 510, y = 575 )
	btn_guardar	=	Button (frame, text = "Guardar", command = lambda: guardar_cuadricula(str(nombre.get()))).place(x = 770, y = 572)
	btn_reset	=	Button (frame, text = "Resetear", command = lambda: personalizar_juego(master,modo_juego)).place(x = 825, y = 572)

	img_cont_minas	=	PhotoImage(file = "Texturas\mina_vector.png")
	lbl_cont_minas	=	Label(frame, image = img_cont_minas).place(x = 825, y = 100)	 
	contador		=	Label(frame, text = contador_minas,width=3, font = ("Arial",25)).place(x = 880, y = 100) 
	matriz_temp 	= 	crear_matriz(cuadricula(modo_juego)+1,cuadricula(modo_juego)+1)
	cuadricula_juego =	crear_botones(master,0,0,coord_x(modo_juego),coord_y(modo_juego),cuadricula(modo_juego),modo_juego,False)
	master.mainloop()	

#E: Un número entero
#S: Un cuadro de dialogo dependiendo del número
#R: El número debe estar entre 1 y 3
def cuadro_eventos(master,modo_juego,evento):
	if evento == 1:
		return messagebox.showinfo("Seleccionado", "¡Se ha seleccionado la cuadrícula! ")
	elif evento == 2:
		messagebox.showinfo("¡Ganaste!", "¡Has ganado! ☺")
		return regresar_reiniciar(master,modo_juego,False)
	elif evento == 3:
		messagebox.showinfo("¡Perdiste!", "¡Has perdido! ☹")
		return regresar_reiniciar(master,modo_juego,False)

#E: El nombre de la cuadricula (String).
#S: guarda la cuadricula en un txt y el nombre en lista_cuadricula.txt.
#R: nombre debe ser un string.
def guardar_cuadricula(nombre):
	global matriz_temp,contador_minas
	archivo= "Cuadriculas\\" + nombre +".txt"
	if nombre == "":
		return messagebox.showinfo("Error", "¡Debe agregarle un nombre a la cuadricula! ")
	elif contador_minas == 0:
		txt=open (archivo,"a")
		txt2=open ("Cuadriculas\lista_cuadriculas.txt","a")
		txt.write (str(matriz_temp))
		txt2.write (nombre+"\n")
		txt2.close()
		txt.close()
		return messagebox.showinfo("Guardado", "¡Se ha guardado la cuadrícula! ")
	else:	
		return messagebox.showinfo("Error", "¡Debe selecionar la posición de todas las minas! ")

#E: Una ventana y un número.
#S: Abre la ventana con el juego de buscaminas.
#R:	master debe ser un Tk() y modo de juego debe ser un número entero positivo entre 1 y 3.
def jugar(master,modo_juego):
	global matriz_temp
	if matriz_temp == []:
		matriz_juego = crear_matriz (cuadricula(modo_juego)+1,cuadricula(modo_juego)+1)
		matriz_temp = minas_colindantes (matriz_aleatoria(matriz_juego,cant_minas(modo_juego),cuadricula(modo_juego)),0,0)

	frame 		=	preferencias_ventana(master)
	img_fondo 	= 	PhotoImage(file = "Texturas\Fondo.png")
	fondo 		= 	Label(frame, image = img_fondo).place(x = -2, y = -2)	
	botones 	=	crear_botones(master,0,0,coord_x(modo_juego), coord_y(modo_juego),cuadricula(modo_juego),modo_juego,True)
	img_atras 	=	PhotoImage(file = "Texturas\Left-arrow.png")
	boton_atras =	Button(frame, image = img_atras,bg = "#FFFFFF", command = lambda:regresar_reiniciar(master,modo_juego,True)).place(x = 0, y = 0)
	img_ojo		=	PhotoImage(file = "Texturas\ojo.png")
	btn_ojo		=	Button(frame, image = img_ojo,command = lambda:mostrar(master,0,0)).place(x = 630, y = 100)

	img_reiniciar	=	PhotoImage(file = "Texturas\Reiniciar.png")
	btn_reiniciar	=	Button(frame, image = img_reiniciar, command = lambda:regresar_reiniciar(master,modo_juego,False)).place(x = 700, y = 100)
	master.mainloop()

#E: Una ventana (master), un número(modo_juego),un valor booleano(regresar)
#S: Regresa a la ventana principal o reinicia la matriz dependiendo si regresar es verdadero o falso
#R: master debe ser una ventana, modo de juego debe ser un número de 1 a 3 y regresar un valor booleano.
def regresar_reiniciar(master,modo_juego,regresar):
	global botones,matriz_temp,personalizado
	if personalizado != []:
		matriz_temp = personalizado
		botones = []
		if regresar:
			ventana_principal(master,modo_juego)		
		else:
			jugar(master,modo_juego)	
	else:
		matriz_temp = []
		botones = []
		if regresar:
			ventana_principal(master,modo_juego)		
		else:
			jugar(master,modo_juego)		


#E: Matriz y dos números.
#S: Una matriz aleatorea en el caso que no se haya seleccionado una.
#R: matriz_juego debe ser un número, minas debe ser un número entero con la cantidad de minas, cuadricula debe tener el largo de la matriz-1
def matriz_aleatoria(matriz_juego,minas,cuadricula):
	i=random.randint(0,cuadricula)	
	j=random.randint(0,cuadricula)
	if matriz_juego[i][j] ==0:
		if minas == 0:
			matriz_juego[i][j] = 10
			return matriz_juego
		else:
			matriz_juego[i][j] = 10
			return matriz_aleatoria(matriz_juego,minas-1,cuadricula)

	else:
		return matriz_aleatoria(matriz_juego,minas,cuadricula)


#E: Una ventana, una coordenada i, una coordenada j, y una lista con las coordenadas "x", "y" y el modo de juego.
#S: Una cuadricula de botones según el modo de juego.
#R: master debe ser un Tk(), i debe ser 0, j debe ser 0, coord_cuadricula debe ser una lista con tres elementos numéricos enteros.
def crear_botones(master,i,j,x,y,cuadricula,modo_juego,jugar):
	global botones,matriz_temp
	if i == len(matriz_temp):
		return 
	elif jugar:
		if i == cuadricula and j == cuadricula:
			boton = Button(master,width = 3, height = 1, command = lambda: click(master,i,j,cuadricula,modo_juego))
			boton.bind("<Button-3>", lambda e,x=x, y=y, i=i,j=j,cuadricula=cuadricula,modo_juego=modo_juego,master=master:click_derecho(master,i,j,x,y,cuadricula,modo_juego))
			boton.place(x = x , y = y)
			botones[i] +=[boton]
			
		elif j == cuadricula:
			boton = Button(master,width = 3, height = 1, command = lambda: click(master,i,j,cuadricula,modo_juego))
			boton.bind("<Button-3>", lambda e,x=x, y=y, i=i,j=j,cuadricula=cuadricula,modo_juego=modo_juego,master=master:click_derecho(master,i,j,x,y,cuadricula,modo_juego))
			boton.place(x = x , y = y)
			botones[i] +=[boton]
			return crear_botones(master,i+1,0,coord_x(modo_juego),y+25,cuadricula,modo_juego,jugar)
		else:
			boton = Button(master,width = 3, height = 1, command = lambda: click(master,i,j,cuadricula,modo_juego))
			boton.bind("<Button-3>", lambda e,x=x, y=y, i=i,j=j,cuadricula=cuadricula,modo_juego=modo_juego,master=master:click_derecho(master,i,j,x,y,cuadricula,modo_juego))
			boton.place(x = x , y = y)
			if j == 0:
				botones +=[[boton]]
			else:
				botones[i] +=[boton]		
			return crear_botones(master,i,j+1,x+30,y,cuadricula,modo_juego,jugar)	

	else:
		if i == cuadricula and j == cuadricula:
			boton = Button(master,width = 3, height = 1, command = lambda: insertar_bomba(master,i,j,x,y,cuadricula))
			boton.place(x = x , y = y)
			botones[i] +=[boton]
		elif j == cuadricula:
			boton = Button(master,width = 3, height = 1, command = lambda: insertar_bomba(master,i,j,x,y,cuadricula))
			boton.place(x = x , y = y)
			botones[i] +=[boton]
			return crear_botones(master,i+1,0,coord_x(modo_juego),y+25,cuadricula,modo_juego,jugar)
		else:
			boton = Button(master,width = 3, height = 1, command = lambda: insertar_bomba(master,i,j,x,y,cuadricula))
			boton.place(x = x , y = y)				
			if j == 0:
				botones +=[[boton]]
			else:
				botones[i] +=[boton]
			return crear_botones(master,i,j+1,x+30,y,cuadricula,modo_juego,jugar)				

#E: Una ventana,6 números.
#S: Deshabilita y pone una bandera o un signo de pregunta en un botón de la cuadricula 
#R: master debe ser una ventana (TK()), "i" y "j" deben ser posiciones en una matriz, "x" y "y" deben ser las coordenadas en la ventana, cuadricula debe ser el largo de la matriz-1 y modo de juego un número entre 1 y 3
def click_derecho(master,i,j,x,y,cuadricula,modo_juego):
	global matriz_temp,botones
	if botones[i][j]["relief"]!=SUNKEN:

		if botones[i][j]["state"]== "normal" and botones[i][j]["text"] == "" :
			botones[i][j]["text"]="⚑"
			botones[i][j]["bg"]="red"
			botones[i][j]["state"]="disabled"

		elif botones[i][j]["state"]== "disabled" and botones[i][j]["text"] != "?":
			botones[i][j]["text"]="?"
			botones[i][j]["bg"]="gray"
			botones[i][j]["state"]="normal"			

		else:
			botones[i][j]["text"]=""
			botones[i][j]["bg"]="white"
			botones[i][j]["state"]="normal"	
	gane(master,0,0,matriz_temp,modo_juego)		


#E: Una ventana(master), dos indices(i,j), tamaño de la cuadricula(cuadricula) y el modo de juego(un número).
#S: Descubre los valores de la matriz al darle click al botón.
#R: master debe ser una ventana, "i" y "j" deben ser números enteros y modo de juego un número de 1 a 3.
def click(master,i,j,cuadricula,modo_juego):
	global botones,matriz_temp	
	if i == len(matriz_temp):
		return
	elif matriz_temp[i][j] != 0 and matriz_temp[i][j] != 10:
		botones[i][j]["text"]=str(matriz_temp[i][j])
		botones[i][j].config(relief= SUNKEN)
		botones[i][j]['state'] = "disabled"

	elif matriz_temp[i][j] == 0:
		ceros_colindantes(i,j)
	else:
		mostrar_minas(master,0,0,cuadricula,modo_juego)	
	gane(master,0,0,matriz_temp,modo_juego)

#E: Una ventana(master), dos indices(i,j), el tamaño de la cuadrícula(cuadricula) y un número(modo_juego).
#S: Muestra todas las minas de la cuadrícula si se da click a un botón con una mina.
#R: master debe ser una ventana, "i" y "j" deben ser números enteros y modo de juego un número de 1 a 3.
def mostrar_minas(master,i,j,cuadricula,modo_juego):
	global matriz_temp,botones
	if i == cuadricula and j == cuadricula:
		if matriz_temp[i][j] == 10:
			botones[i][j]["bg"]="red"
			botones[i][j]["text"]="✹"
		return cuadro_eventos(master,modo_juego,3)	
	elif j == len(matriz_temp)-1:
		if matriz_temp[i][j] == 10:
			botones[i][j]["bg"]="red"
			botones[i][j]["text"]="✹"
		return mostrar_minas(master,i+1,0,cuadricula,modo_juego)
	else:
		if matriz_temp[i][j] == 10:
			botones[i][j]["bg"]="red"
			botones[i][j]["text"]="✹"		
		return mostrar_minas(master,i,j+1,cuadricula,modo_juego)		

#E: Una ventana, dos indices(i,j), una matriz(matriz) y un número(modo_juego).
#S: una ventana de gane si todos los botones están deshabilitados
#R: master debe ser una ventana, "i" y "j" deben ser números enteros, modo de juego debe ser un número entero entre 1 y 3.
def gane(master,i,j,matriz,modo_juego):
	global botones
	if i== len(matriz)-1 and j == len(matriz)-1:
		return cuadro_eventos(master,modo_juego,2)
	elif matriz[i][j] == 10:
		if i==len(matriz):
			return		
		elif botones[i][j]["state"] == "disabled" and j == len(matriz)-1:
			return gane(master,i+1,0,matriz,modo_juego)
		elif botones[i][j]["state"] == "disabled":
			return gane(master,i,j+1,matriz,modo_juego)
		else:
			return 

	else:	
		if i==len(matriz):
			return
		elif botones[i][j]["state"] == "disabled" and j == len(matriz)-1:
			return gane(master,i+1,0,matriz,modo_juego)
		elif botones[i][j]["state"] == "disabled":
			return gane(master,i,j+1,matriz,modo_juego)
		else:
			return False




#E: Dos índices(i,j).
#S: Descubre los botones que están al rededor si se le da click a una posición en la matriz con ceros.
#R: "i" y "j" son números enteros positivos.
def ceros_colindantes(i,j):
	global matriz_temp,botones
	if botones[i][j]["state"] == "disabled":
		return
	if matriz_temp[i][j] != 0:
		botones[i][j]["text"] = str(matriz_temp[i][j])
	botones[i][j].config(relief=SUNKEN)
	botones[i][j]['state'] = 'disabled'	
	if matriz_temp[i][j] == 0:
		if i != 0 and j != 0:
			ceros_colindantes(i-1,j-1)
		if i != 0:
			ceros_colindantes(i-1,j)
		if i != 0 and j != len(matriz_temp)-1:
			ceros_colindantes(i-1,j+1)
		if j != 0:
			ceros_colindantes(i,j-1)
		if j != len(matriz_temp)-1:
			ceros_colindantes(i,j+1)
		if i != len(matriz_temp)-1 and j != 0:
			ceros_colindantes(i+1,j-1)
		if i != len(matriz_temp)-1:
			ceros_colindantes(i+1,j)
		if i != len(matriz_temp)-1 and j != len(matriz_temp)-1:
			ceros_colindantes(i+1,j+1)	


#E: Una matriz(matriz) y dos idices(i,j)
#S: Le otorga un valor a la matriz dependiendo de la cantidad de minas colindantes.
#R:	matriz debe ser una matriz con números enteros. "i" y "j" deben ser número enteros positivos.
def minas_colindantes(matriz,i,j):
	if i==len(matriz)-1 and j == len(matriz)-1:
		if matriz[i][j] != 10:
			matriz[i][j]=sumar_minas(matriz,i,j,0)
		return matriz
	elif j == len(matriz)-1:
		if matriz[i][j] != 10:
			matriz[i][j]=sumar_minas(matriz,i,j,0)
		return minas_colindantes(matriz,i+1,0)
	else:
		if matriz[i][j] != 10:
			matriz[i][j]=sumar_minas(matriz,i,j,0)
		return minas_colindantes(matriz,i,j+1)
	
	
#E: Una matriz(matriz), dos índices(i,j) y un contador.
#S: Suma la cantidad de minas que hay al rededor de un indice
#R: matriz debe ser una matriz con números enteros. "i" y "j" deben ser número enteros positivos, cont debe ser 0
def sumar_minas(matriz,i,j,cont):
	if i==0:
		if j == 0:
			if matriz[i][j+1] == 10:
				cont+=1
			if matriz[i+1][j+1] == 10:
				cont+=1
			if matriz[i+1][j] == 10:
				cont+=1
			return cont

		elif j>0 and j<len(matriz)-1:
			if matriz[i][j+1] == 10:
				cont+=1
			if matriz[i+1][j+1] == 10:
				cont+=1
			if matriz[i+1][j] == 10:
				cont+=1
			if matriz[i+1][j-1] == 10:
				cont+=1
			if matriz[i][j-1] == 10:
				cont+=1
			return cont
		else:
			if matriz[i][j-1] == 10:
				cont+=1
			if matriz[i+1][j-1] == 10:
				cont+=1
			if matriz[i+1][j] == 10:
				cont+=1
			return cont

	elif i > 0 and i < len(matriz)-1:
		if j == 0:
			if matriz[i+1][j] == 10:
				cont+=1
			if matriz[i+1][j+1] == 10:
				cont+=1
			if matriz[i][j+1] == 10:
				cont+=1
			if matriz[i-1][j+1] == 10:
				cont+=1
			if matriz[i-1][j] == 10:
				cont+=1
			return cont

		elif j > 0 and j<len(matriz)-1:
			if matriz[i+1][j-1] == 10:
				cont+=1
			if matriz[i][j-1] == 10:
				cont+=1
			if matriz[i-1][j-1] == 10:
				cont+=1
			if matriz[i-1][j] == 10:
				cont+=1
			if matriz[i-1][j+1] == 10:
				cont+=1
			if matriz[i][j+1] == 10:
				cont+=1
			if matriz[i+1][j+1] == 10:
				cont+=1
			if matriz[i+1][j] == 10:
				cont+=1
			return cont

		else:
			if matriz[i+1][j] == 10:
				cont+=1
			if matriz[i+1][j-1] == 10:
				cont+=1
			if matriz[i][j-1] == 10:
				cont+=1
			if matriz[i-1][j-1] == 10:
				cont+=1
			if matriz[i-1][j] == 10:
				cont+=1
			return cont


	elif i == len(matriz)-1:
		if j == 0:
			if matriz[i-1][j] == 10:
				cont+=1
			if matriz[i-1][j+1] == 10:
				cont+=1
			if matriz[i][j+1] == 10:
				cont+=1
			return cont

		elif j>0 and j<len(matriz)-1:
			if matriz[i][j-1] == 10:
				cont+=1
			if matriz[i-1][j-1] == 10:
				cont+=1
			if matriz[i-1][j] == 10:
				cont+=1
			if matriz[i-1][j+1] == 10:
				cont+=1
			if matriz[i][j+1] == 10:
				cont+=1
			return cont
		else:
			if matriz[i][j-1] == 10:
				cont+=1
			if matriz[i-1][j-1] == 10:
				cont+=1
			if matriz[i-1][j] == 10:
				cont+=1
			return cont

#E: Una ventana(master), dos índices(i,j), un "x" y "y" en la ventana (x,y) y el tamaño de una cuadrícula(cuadricula)
#S: Inserta una bomba en una matriz si no hay ninguna mina anteriormente insertada.
#R: master debe ser una ventana, "i", "j","x" y "y" son números enteros positivos y cuadrícula es un número entero del 1 al 3. 
def insertar_bomba(master,i,j,x,y,cuadricula):
	global contador_minas
	if contador_minas >0 :
		contador_minas -=1
		Label(master, text = contador_minas,width=3, font = ("Arial",25)).place(x = 880, y = 100)
		return actualizar_tablero(master,i,j,x,y,cuadricula)
	master.mainloop()

#E: Una ventana(master), dos índices(i,j), un "x" y "y" en la ventana (x,y) y el tamaño de una cuadrícula(cuadricula)
#S: actualiza tablero el tablero 
#R: master debe ser una ventana, "i", "j","x" y "y" son números enteros positivos y cuadrícula es un número entero del 1 al 3. 
def actualizar_tablero(master,i,j,x,y,cuadricula):
	global matriz_temp
	matriz_temp [i][j] = 10
	mina = PhotoImage(file = "Texturas\mina_vector1.png")
	boton = Button(master,image=mina,width= 24).place(x = x, y = y)
	master.mainloop()

#E: Dos números(columnas,filas).
#S: Crea una matriz con ceros según la cantidad de filas y columnas.
#R: Columnas y filas deben ser números enteros.
def crear_matriz(columnas,filas):
	if filas == 0:
		return []
	else:
		return [crear_filas(columnas)]+crear_matriz(columnas,filas-1)

#E: Un número(columnas)
#S: Crea un vector según la cantidad de columnas
#R: Columnas debe ser un número entero
def crear_filas(columnas):
	if columnas == 0:
		return []
	else:
		return [0]+crear_filas(columnas-1)
	
#E: Un número 
#S: una lista con las coordenadas "x", "y" y la cuadricula
#R: modo_juego debe ser un número
def cuadricula(modo_juego):
	if modo_juego == 3:
		return 15
	elif modo_juego == 2:
		return 9
	elif modo_juego == 1:
		return 4
	elif modo_juego == 16:
		return 3
	elif modo_juego == 10:
		return 2
	else:
		return 1

#E: Un número.
#S: La coordenada "x" según el modo de juego.
#R. cuadricula debe ser 3,2 ó 1.
def coord_x(modo_juego):
	if modo_juego == 3:
		return 420
	elif modo_juego ==2:
		return 500
	else:
		return 600

#E: Un número
#S: la coordenada "y" según el modo de juego.
#R. modo_juego debe ser un número entero positivo entre 1 y 3.
def coord_y(modo_juego):
	if modo_juego == 3:
		return 150
	elif modo_juego ==2:
		return 200
	elif modo_juego == 1:
		return 250

#E: Un número.
#S: El número de minas segun el juego.
#R: modo_juego debe ser un número entero positivo entre 1 y 3.
def cant_minas(modo_juego):
	if modo_juego == 1:
		return 5
	elif modo_juego == 2:
		return 10
	elif modo_juego == 3:
		return 25

ventana_principal(Tk(),1)
