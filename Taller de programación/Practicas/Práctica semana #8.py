##Recursividad Cola
##
##>>>eliminar_elemento([2,5,7,2,3],2)
##    [5,7,3]
##
##>>>buscar_elemento([1,4,2,3,4,7],4)
##    [1,4]
##
##>>>invertir([1,2,3,4])
##    [4,3,2,1]
##
##>>>ordenar([4,2,1,7,6])
##    [1,2,4,6,7]


#E:Una lista un elemento
#S:Eliminar el número que se desea(elemento)
#R:lista debe ser una lista y el elemento debe ser un número entero
def eliminar_elemento(lista,elemento):
    if isinstance(lista,list):
        if isinstance(elemento,int):
            return eliminar_elementoAux(lista,elemento,[])
        else:
            print("El elemento no es un número entero")
    else:
        print("Lista no es una lista")
        
def eliminar_elementoAux(lista,elemento,resultado):
    if lista==[]:
        return resultado
    elif lista[0]!=elemento:
        return eliminar_elementoAux(lista[1:],elemento,resultado+[lista[0]])
    else:
        return eliminar_elementoAux(lista[1:],elemento,resultado)
                                

#E:Una lista(lista) y un elemento(elemento)
#S:La posición en la que se encuentra el elmento
#R:lista debe ser una lista y elemento un número entero
def buscar_elemento(lista,elemento):
    if isinstance(lista,list):
        if isinstance(elemento,int):
            return buscar_elementoAux(lista,elemento,0,[])
        else:
            print("El elemento no es un número entero")
    else:
        print("Lista no es una lista")

def buscar_elementoAux(lista,elemento,posicion,resultado):
    if lista==[]:
        return resultado
    elif lista[0]==elemento:
        return buscar_elementoAux(lista[1:],elemento,posicion+1,resultado+[posicion])
    else:
        return buscar_elementoAux(lista[1:],elemento,posicion+1,resultado)
        
#E:Una lista(lista)
#S:invertir los elementos de la lista 
#R:lista debe ser una lista
def invertir(lista):
    if isinstance(lista,list):
        return invertirAux(lista,[])
    else:
        print("Lista no es una lista")
def invertirAux(lista,resultado):
    if lista==[]:
        return resultado
    else:
            return invertirAux(lista[0:-1],resultado+[lista[-1]])
    
#E:Una lista(lista)
#S:ordenar los elementos de la lista 
#R:lista debe ser una lista,los elementos de la lista deben ser números enteros
def ordenar(lista):
    if isinstance(lista,list):
        return ordenarAux(lista,[])
    else:
        print("Lista no es una lista")
def ordenarAux(lista,resultado):
    if entero(lista):        
        if lista==[]:
            return resultado
        elif menor(lista,lista[0]):
            
            return ordenarAux(lista[1:],resultado+[lista[0]])
        else:
            return ordenarAux(lista[1:]+[lista[0]],resultado)
    else:
        return "Los elementos de lista no son números enteros"           


def menor(lista,elemento):
        if lista==[]:
            return True
        elif lista[0]<elemento:
            return False
        else:
            return menor(lista[1:],elemento)
        
def entero(lista):
    if lista==[]:
        return True
    elif isinstance(lista[0],int):
        return entero(lista[1:])
    else:
       return False   
        
