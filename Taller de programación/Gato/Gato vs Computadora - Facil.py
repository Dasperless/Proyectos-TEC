from tkinter import *
from tkinter import  messagebox
from tkinter import ttk
from random import randint
matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

jugador = 1

def reiniciar_matriz(main,rol):
    global matriz,jugador
    matriz = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    jugador = 1

    if rol == 0:
        vs_jugador(main)
    else:
        vs_computadora(main)
    
def cambiar_turno():
    global jugador
    if jugador == 1:
        jugador += 1
    else:
        jugador -= 1


def obtener_columna(matriz):
    if matriz==[]:
        return []
    else:
        return [matriz[0][0]]+obtener_columna(matriz[1:])

def quitar_columna(matriz):
    if matriz==[]:
        return []
    else:
        return [matriz[0][1:]]+quitar_columna(matriz[1:])

def obtener_columna_inv(matriz):
    if matriz==[]:
        return []
    else:
        return [matriz[0][-1]]+obtener_columna_inv(matriz[1:])

def quitar_columna_inv(matriz):
    if matriz==[]:
        return []
    else:
        return [matriz[0][0:-1]]+quitar_columna_inv(matriz[1:])
    
def obtener_diagonal(matriz):
    if matriz == []:
        return []
    else:
        return [matriz[0][0]]+obtener_diagonal(quitar_columna(matriz[1:]))

def obtener_diagonal_inv(matriz):
    if matriz == []:
        return []
    else:
        return [matriz[0][-1]]+obtener_diagonal_inv(quitar_columna_inv(matriz[1:]))    
    
def gano(matriz,main,rol):
    if gane_horizontal(matriz):
        return True
    elif gane_vertical(matriz):
        return True
    elif gane_diagonal(matriz) or gane_diagonal_inv(matriz):
        return True
    elif empate(matriz):
        messagebox.showinfo("¡Empate!", "Se ha empatado")        
        return reiniciar_matriz(main,rol)
    else:
        return False
    
def empate(matriz):
    if matriz == []:
        return True
    elif matriz[0] == []:
        return empate(matriz[1:])
    elif comprobar_ceros(matriz[0]):
        return False
    else:
        return empate(matriz[1:])

def comprobar_ceros(lista):
    if lista == []:
        return False
    elif lista[0] == 0:
        return True
    else:
        return comprobar_ceros(lista[1:])
    
def quitar_elemento(matriz):
    matriz[0]=matriz[0][1:]
    return matriz

def gane_horizontal(matriz):
    if matriz == []:
        return False
    elif matriz [0] == [1,1,1] or matriz[0] == [2,2,2]:
        return True
    else:
        return gane_horizontal(matriz[1:])   
    
def gane_vertical(matriz):
    if matriz[0] == []:
        return False
    elif obtener_columna(matriz) == [1,1,1] or obtener_columna(matriz) == [2,2,2]:
        return True
    else:
        return gane_vertical(quitar_columna(matriz))

def gane_diagonal(matriz):
    if obtener_diagonal(matriz) == [1,1,1] or obtener_diagonal(matriz) == [2,2,2]:
        return True
    else:
        return False
    
def gane_diagonal_inv(matriz):
    if obtener_diagonal_inv(matriz) == [1,1,1] or obtener_diagonal_inv(matriz) == [2,2,2]:
        return True
    else:
        return False    
    
    
def modificar_matriz(posicion,main,rol):
    global matriz,jugador
    i = posicion[0]
    j = posicion[1]
    
    if jugador == 1 and matriz[i][j] == 0:
        turno = Label(main,text="Turno de : O").grid(row=1,column=0,columnspan=2)        
    elif jugador == 2 and matriz[i][j] == 0:
        turno = Label(main,text="Turno de : X").grid(row=1,column=0,columnspan=2)
    else:
        return messagebox.showinfo("Movimiento inválido", "No se puede selecionar esa casilla")
        
    matriz[i][j] = jugador
    cambiar_botones([i,j],jugador,main)
    
    if gano(matriz,main,rol):
        if jugador == 1:
            messagebox.showinfo("¡Gano!", "Las 'X' ganaron ")
            return reiniciar_matriz(main,rol)
        else:
            messagebox.showinfo("¡Gano!", "Las 'O' ganaron ")
            return reiniciar_matriz(main,rol)
        
    cambiar_turno()

def modificar_matriz_pc(posicion,main,rol):
    modificar_matriz(posicion,main,rol)
    computadora(main,posicion,matriz,rol)

def indice(pos):
    i=randint(pos[0],pos[1])
    return i

def movida(main,pos,matriz,rol):
    i = indice(pos[0])
    j = indice(pos[1])
    if matriz[i][j] == 0:
        return modificar_matriz([i,j],main,rol)
    else:
        return computadora(main,[i,j],matriz,rol)
    
def computadora(main,posicion,matriz,rol):
    if posicion == [0,0]:
        return movida (main,[[0,1],[0,1]],matriz,rol)
    elif posicion == [0,1]:
        return movida (main,[[0,1],[0,2]],matriz,rol)
    elif posicion == [0,2]:
        return movida (main,[[0,1],[1,2]],matriz,rol)
    elif posicion == [1,0]:
        return movida (main,[[0,2],[0,1]],matriz,rol)
    elif posicion == [1,1]:
        return movida (main,[[0,2],[0,2]],matriz,rol)
    elif posicion == [1,2]:
        return movida (main,[[0,2],[1,2]],matriz,rol)
    elif posicion == [2,0]:
        return movida (main,[[1,2],[0,1]],matriz,rol)
    elif posicion == [2,1]:
        return movida (main,[[1,2],[0,2]],matriz,rol)
    elif posicion == [2,2]:
        return movida (main,[[1,2],[1,2]],matriz,rol)    

        
        
        
    
def vs_jugador(main):
    titulo = Label(main,text="Gato",width=20).grid(columnspan=3,row=0,column=0)
    turno = Label(main,text="Turno de : X").grid(row=1,column=0,columnspan=2)
    
    #Botones matriz[0][0:]
    b_0_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([0,0],main,0)).grid(row = 3,column = 0,columnspan = 1)

    b_0_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([0,1],main,0)).grid(row = 3,column = 1,columnspan = 1)

    b_0_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([0,2],main,0)).grid(row = 3,column = 2,columnspan = 1)
 
    #Botones matriz[1][0:]
    b_1_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,0],main,0)).grid(row = 4,column = 0,columnspan = 1)

    b_1_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,1],main,0)).grid(row = 4,column = 1,columnspan = 1)

    b_1_2 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,2],main,0)).grid(row = 4,column = 2,columnspan = 1)

    #Botones matriz[2][0:]
    b_2_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([2,0],main,0)).grid(row = 5,column = 0,columnspan = 1)

    b_2_1 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([2,1],main,0)).grid(row = 5,column = 1,columnspan = 1)

    b_2_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([2,2],main,0)).grid(row = 5,column = 2,columnspan = 1)


    #Botones de menu

    Reiniciar = ttk.Button(main,text="Reiniciar",width = 7,command = lambda:reiniciar_matriz(main,0)).grid(row = 7,column = 0)
    Salir = ttk.Button(main,text="Salir", width = 7,command = lambda:quit()).grid(row = 7,column = 1,columnspan=1)


def vs_computadora(main):
    titulo = Label(main,text="Gato",width=20).grid(columnspan=3,row=0,column=0)
    turno = Label(main,text="Turno de : X").grid(row=1,column=0,columnspan=2)    
    
    #Botones matriz[0][0:]
    b_0_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([0,0],main,1)).grid(row = 3,column = 0,columnspan = 1)

    b_0_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([0,1],main,1)).grid(row = 3,column = 1,columnspan = 1)

    b_0_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz_pc([0,2],main,1)).grid(row = 3,column = 2,columnspan = 1)
 
    #Botones matriz[1][0:]
    b_1_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([1,0],main,1)).grid(row = 4,column = 0,columnspan = 1)

    b_1_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([1,1],main,1)).grid(row = 4,column = 1,columnspan = 1)

    b_1_2 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([1,2],main,1)).grid(row = 4,column = 2,columnspan = 1)

    #Botones matriz[2][0:]
    b_2_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz_pc([2,0],main,1)).grid(row = 5,column = 0,columnspan = 1)
    
    b_2_1 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz_pc([2,1],main,1)).grid(row = 5,column = 1,columnspan = 1)

    b_2_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz_pc([2,2],main,1)).grid(row = 5,column = 2,columnspan = 1)


    #Botones de menu

    Reiniciar = ttk.Button(main,text="Reiniciar",width = 7,command = lambda:reiniciar_matriz(main,1)).grid(row = 7,column = 0)
    Salir = ttk.Button(main,text="Salir", width = 7,command = lambda:main.destroy()).grid(row = 7,column = 1,columnspan=1)


def cambiar_botones(pos,jugador,main):
    if jugador == 1:
        if pos == [0,0]:
            b_0_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,0],main,-1)).grid(row = 3,column = 0,columnspan = 1)
            
        elif pos == [0,1]:
            b_0_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,1],main,-1)).grid(row = 3,column = 1,columnspan = 1)
            
        elif pos == [0,2]:
            b_0_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,2],main,-1)).grid(row = 3,column = 2,columnspan = 1)
            
        elif pos == [1,0]:
            b_1_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,0],main,-1)).grid(row = 4,column = 0,columnspan = 1)

        elif pos == [1,1]:
            b_1_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,1],main,-1)).grid(row = 4,column = 1,columnspan = 1)

        elif pos == [1,2]:
            b_1_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,2],main,-1)).grid(row = 4,column = 2,columnspan = 1)

        elif pos == [2,0]:
            b_2_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,0],main,-1)).grid(row = 5,column = 0,columnspan = 1)

        elif pos == [2,1]:
            b_2_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,1],main,-1)).grid(row = 5,column = 1,columnspan = 1)            

        elif pos == [2,2]:
            b_2_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,2],main,-1)).grid(row = 5,column = 2,columnspan = 1)
    else:
        if pos == [0,0]:
            b_0_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,0],main,-1)).grid(row = 3,column = 0,columnspan = 1)
            
        elif pos == [0,1]:
            b_0_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,1],main,-1)).grid(row = 3,column = 1,columnspan = 1)
            
        elif pos == [0,2]:
            b_0_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,2],main,-1)).grid(row = 3,column = 2,columnspan = 1)
            
        elif pos == [1,0]:
            b_1_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,0],main,-1)).grid(row = 4,column = 0,columnspan = 1)

        elif pos == [1,1]:
            b_1_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,1],main,-1)).grid(row = 4,column = 1,columnspan = 1)

        elif pos == [1,2]:
            b_1_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,2],main,-1)).grid(row = 4,column = 2,columnspan = 1)

        elif pos == [2,0]:
            b_2_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,0],main,-1)).grid(row = 5,column = 0,columnspan = 1)

        elif pos == [2,1]:
            b_2_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,1],main,-1)).grid(row = 5,column = 1,columnspan = 1)            

        elif pos == [2,2]:
            b_2_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,2],main,-1)).grid(row = 5,column = 2,columnspan = 1)
            

#------ Menu principal

def menu_principal(main):
    titulo = Label(main, text = "Juego del gato",font = ("Aral",20)).pack()
    img_inicio = PhotoImage(file = "img_inicio.png")
    imagen = Label(main, image = img_inicio).pack()

    modo_jugador = ttk.Button(main,text= "Jugar contra un amigo", command = lambda:vs_jugador(Toplevel(main))).pack()
    modo_computadora = ttk.Button(main, text= "Jugar contra computadora",command = lambda:vs_computadora(Toplevel(main))).pack()
    salir= ttk.Button(main, text= "Salir",command = lambda:quit()).pack()
    main.mainloop() 

ventana=Tk()
menu_principal(ventana)