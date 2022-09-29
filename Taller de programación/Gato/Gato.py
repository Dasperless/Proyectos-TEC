from tkinter import *
from tkinter import  messagebox

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

jugador = 1

def reiniciar_matriz(main):
    global matriz,jugador
    matriz = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    jugador = 1
    
    crear_ventana(main)
    
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
    
def gano(matriz,main):
    if gane_horizontal(matriz):
        return True
    elif gane_vertical(matriz):
        return True
    elif gane_diagonal(matriz) or gane_diagonal_inv(matriz):
        return True
    elif empate(matriz):
        messagebox.showinfo("¡Empate!", "Se ha empatado")        
        return reiniciar_matriz(main)
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
    
    
def modificar_matriz(posicion,main):
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
    
    if gano(matriz,main):
        if jugador == 1:
            messagebox.showinfo("¡Gano!", "Las 'X' ganaron ")
            return reiniciar_matriz(main)
        else:
            messagebox.showinfo("¡Gano!", "Las 'O' ganaron ")
            return reiniciar_matriz(main)
        
    cambiar_turno()
    
def crear_ventana(main):
    titulo = Label(main,text="Gato",width=20).grid(columnspan=3,row=0,column=0)
    turno = Label(main,text="Turno de : X").grid(row=1,column=0,columnspan=2)
    
    #Botones matriz[0][0:]
    b_0_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([0,0],main))
    b_0_0.grid(row = 3,column = 0,columnspan = 1)

    b_0_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([0,1],main))
    b_0_1.grid(row = 3,column = 1,columnspan = 1)

    b_0_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([0,2],main))
    b_0_2.grid(row = 3,column = 2,columnspan = 1)
 
    #Botones matriz[1][0:]
    b_1_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,0],main))
    b_1_0.grid(row = 4,column = 0,columnspan = 1)

    b_1_1 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,1],main))
    b_1_1.grid(row = 4,column = 1,columnspan = 1)

    b_1_2 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([1,2],main))
    b_1_2.grid(row = 4,column = 2,columnspan = 1)

    #Botones matriz[2][0:]
    b_2_0 = Button(main,width = 6,height = 2,command = lambda:modificar_matriz([2,0],main))
    b_2_0.grid(row = 5,column = 0,columnspan = 1)

    b_2_1 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([2,1],main))
    b_2_1.grid(row = 5,column = 1,columnspan = 1)

    b_2_2 = Button(main,width = 6,height = 2,command=lambda:modificar_matriz([2,2],main))
    b_2_2.grid(row = 5,column = 2,columnspan = 1)


    #Botones de menu

    Reiniciar = Button(main,text="Reiniciar",width = 6,command = lambda:reiniciar_matriz(main)).grid(row = 7,column = 0)
    Salir = Button(main,text="Salir", width = 6,command = lambda:main.destroy()).grid(row = 7,column = 1,columnspan=1)

def cambiar_botones(pos,jugador,main):
    if jugador == 1:
        if pos == [0,0]:
            b_0_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,0],main))
            b_0_0.grid(row = 3,column = 0,columnspan = 1)
            
        elif pos == [0,1]:
            b_0_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,1],main))
            b_0_1.grid(row = 3,column = 1,columnspan = 1)
            
        elif pos == [0,2]:
            b_0_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([0,2],main))
            b_0_2.grid(row = 3,column = 2,columnspan = 1)
            
        elif pos == [1,0]:
            b_1_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,0],main))
            b_1_0.grid(row = 4,column = 0,columnspan = 1)

        elif pos == [1,1]:
            b_1_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,1],main))
            b_1_1.grid(row = 4,column = 1,columnspan = 1)

        elif pos == [1,2]:
            b_1_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([1,2],main))
            b_1_2.grid(row = 4,column = 2,columnspan = 1)

        elif pos == [2,0]:
            b_2_0 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,0],main))
            b_2_0.grid(row = 5,column = 0,columnspan = 1)

        elif pos == [2,1]:
            b_2_1 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,1],main))
            b_2_1.grid(row = 5,column = 1,columnspan = 1)            

        elif pos == [2,2]:
            b_2_2 = Button(main, text="X", width = 6,height = 2,command = lambda:modificar_matriz([2,2],main))
            b_2_2.grid(row = 5,column = 2,columnspan = 1)
    else:
        if pos == [0,0]:
            b_0_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,0],main))
            b_0_0.grid(row = 3,column = 0,columnspan = 1)
            
        elif pos == [0,1]:
            b_0_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,1],main))
            b_0_1.grid(row = 3,column = 1,columnspan = 1)
            
        elif pos == [0,2]:
            b_0_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([0,2],main))
            b_0_2.grid(row = 3,column = 2,columnspan = 1)
            
        elif pos == [1,0]:
            b_1_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,0],main))
            b_1_0.grid(row = 4,column = 0,columnspan = 1)

        elif pos == [1,1]:
            b_1_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,1],main))
            b_1_1.grid(row = 4,column = 1,columnspan = 1)

        elif pos == [1,2]:
            b_1_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([1,2],main))
            b_1_2.grid(row = 4,column = 2,columnspan = 1)

        elif pos == [2,0]:
            b_2_0 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,0],main))
            b_2_0.grid(row = 5,column = 0,columnspan = 1)

        elif pos == [2,1]:
            b_2_1 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,1],main))
            b_2_1.grid(row = 5,column = 1,columnspan = 1)            

        elif pos == [2,2]:
            b_2_2 = Button(main, text="O", width = 6,height = 2,command = lambda:modificar_matriz([2,2],main))
            b_2_2.grid(row = 5,column = 2,columnspan = 1)
            
  
    
    
    









ventana=Tk()
crear_ventana(ventana)
