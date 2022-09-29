##1
#E: Una lista.
#S: Una lista con dos elementos sublista. La primer sublista es la lista en el mismo orden sin números repetidos.La segunda sublista es la primer sublista modificada, donde los númerosparecen ordenados ascendentemente.
#R: La lista debe contener números enteros positivos

##Versión iterativa
def procesa_listaI(lista):
    if isinstance(lista,list):
        if lista == []:
            print("La lista está vacía")
        elif entero_positivoI(lista):
            res=[]
            while lista!=[]:
                if not repetidoI(res,lista[0]):
                    res+=[lista[0]]
                lista=lista[1:]
            return [res,ordenarI(res)]
                    
        else:
            print("Los elementos de la lista debe ser números enteros y positivos")
    else:
        print("La variable ingresado no es una lista")

def repetidoI(lista,n):
    while lista !=[]:
        if lista[0] == n:
            return True
        lista = lista[1:]
    return False

def entero_positivoI(lista):
    while lista!=[]:
        if lista[0]>=0 and isinstance(lista[0],int):
            lista = lista[1:]
        else:
            return False
    return True

def menorI(lista,n):
    while lista!=[]:
        if n < lista[0]:
            lista=lista[1:]
        else:
            return False
    return True

def ordenarI(lista):
    res=[]
    while lista!=[]:
        if menorI(lista[1:],lista[0]):
            res+=[lista[0]]
            lista=lista[1:]
        else:
            lista=lista[1:]+[lista[0]]
    return res

##Versión recursiva
def procesa_listaR(lista):
    if isinstance(lista,list):
        if lista == []:
            print("La lista está vacía")
        elif entero_positivoR(lista):
            return procesa_listaAuxR(lista,[])      
        else:
            print("Los elementos de la lista debe ser números enteros y positivos")
    else:
        print("La variable ingresada no es una lista")
        
def procesa_listaAuxR(lista,res):
    if lista==[]:
        return [res,ordenarR(res,[])]
    elif not repetidoR(res,lista[0]):
        return procesa_listaAuxR(lista[1:],res+[lista[0]])
    else:
        return procesa_listaAuxR(lista[1:],res)
    
def repetidoR(lista,n):
    if lista==[]:
        return False
    elif lista[0] == n:
        return True
    else:
        return repetidoR(lista[1:],n)
    
def entero_positivoR(lista):
    if lista==[]:
        return True
    elif lista[0]>=0 and isinstance(lista,list):
        return entero_positivoR(lista[1:])
    else:
        return False

def menorR(lista,n):
    if lista==[]:
        return True
    elif n < lista[0]:
        return menorR(lista[1:],n)
    else:
        return False
    
def ordenarR(lista,res):
    if lista==[]:
        return res
    elif menorR(lista[1:],lista[0]):
        return ordenarR(lista[1:],res+[lista[0]])
    else:
        return ordenarR(lista[1:]+[lista[0]],res)
##2
#E: Una matriz
#S: True si la matriz ingresada representa la matriz identidad y False en caso contrario
#R: La matriz debe ser cuadrada. La matriz debe contener números enteros positivos
    
##Versión Iterativa
def matriz_identidadI(matriz):
    if isinstance(matriz,list):
        if matrizEntPosI(matriz):
            if cuadradaI(matriz):
                for i in range(largoFilasI(matriz)):
                    for j in range(largoFilasI(matriz)):
                        if i==j and matriz[i][j] != 1:
                            return False
                        elif i!=j and matriz[i][j]!=0:
                            return False
                return True           
                        
            else:
                print("La matriz no es cuadrada")
        else:
            print("Los elementos de la matriz no son números enteros positivos")
    else:
        print("La variable ingresada no es una matriz")
        
def largoFilasI(matriz):
    largo=0
    for i in matriz[0]:
        largo+=1
    return largo

def largoColumnasI(matriz):
    largo=0
    for i in matriz:
        largo+=1
    return largo

def cuadradaI(matriz):
    if largoFilasI(matriz)==largoColumnasI(matriz):
        return True
    else:
        return False
              
def matrizEntPosI(matriz):
    for i in range(largoFilasI(matriz)):
        for j in range(largoFilasI(matriz)):
            if not isinstance(matriz[i][j],int) or matriz[i][j]<0:
              return False
    return True

##Versión recursiva                
def matriz_identidadR(matriz):
    if isinstance(matriz,list):
        if matrizEntPosI(matriz):
            if cuadradaI(matriz):
                return matriz_identidadRAux(matriz,0,0)          
            else:
                print("La matriz no es cuadrada")
        else:
            print("Los elementos de la matriz no son números enteros positivos")
    else:
        print("La variable ingresada no es una matriz")
        
def matriz_identidadRAux(matriz,i,j):
    if largoFilasR(matriz) == i+1 and largoFilasR(matriz) == j:
        return True
    elif j == largoFilasR(matriz):
        return matriz_identidadRAux(matriz,i+1,0)
    elif i!=j and matriz[i][j] == 0:
        return matriz_identidadRAux(matriz,i,j+1)    
    elif i == j and matriz[i][j] == 1:
        return matriz_identidadRAux(matriz,i,j+1)
    else:
        return False
    
def largoFilasR(matriz):
    return largoFilasRAux(matriz[0])

def largoFilasRAux(matriz):
    if matriz == []:
        return 0
    else:
        return 1+largoFilasRAux(matriz[1:])
    
def largoColumnasR(matriz):
    if matriz == []:
        return 0
    else:
        return 1+largoColumnasR(matriz[1:])

def cuadradaR(matriz):
    if largoFilasR(matriz)==largoColumnasR(matriz):
        return True
    else:
        return False

def matrizEntPosR(matriz):
    return matrizEntPosRAux(matriz,0,0)

def matrizEntPosRAux(matriz,i,j):    
    if largoColumnasR(matriz) == i+1 and largoColumnasR(matriz) == j:
        return True
    elif largoColumnasR(matriz) == j:
        return matrizEntPosRAux(matriz,i+1,0)
    elif isinstance (matriz[i][j],int) and matriz[i][j] >= 0:
        return matrizEntPosRAux(matriz,i,j+1)
    else:
        return False

##3
#E: Dos matrices
#S: La suma de ambas matrices
#R: Los elementos de las matrices deben ser números. Las matrices deben ser válidas.

##Versión Iterativa            

def sum_matI(matriz1,matriz2):
    if matriz1!=[] or matriz1!=[[]] or matriz2!=[] or matriz2!=[[]] :
        if isinstance(matriz1,list) and isinstance(matriz2,list):
            if validaI(matriz1,matriz2):
                res=[]
                for i in range(largoFilasI(matriz1)):
                    res+=[sum_filasI(matriz1[i],matriz2[i])]
                return res
                               
            else:
                print("Las matrices deben ser válidas")
        else:
            print("Las entradas que se ingresaron no son matrices")
    else:
        print("Las matrices no pueden estar vacías")
        
def largoListaI(lista):
    res=0
    while lista!=[]:
        lista=lista[1:]
        res+=1
    return res
        
def sum_filasI(fila1,fila2):
    res=[]
    for i in range(largoListaI(fila1)):
        res+=[fila1[i]+fila2[i]]
        
    return res

def validaI(matriz1,matriz2):
    if largoFilasI(matriz1) == largoFilasI(matriz2) and largoColumnasI(matriz1) == largoColumnasI(matriz2):
        return True
    else:
        return False

##Versión recursiva
def sum_matR(matriz1,matriz2):
    if matriz1!=[] or matriz1!=[[]] or matriz2!=[] or matriz2!=[[]] :
        if isinstance(matriz1,list) and isinstance(matriz2,list):
            if validaR(matriz1,matriz2):
                return sum_matRAux(matriz1,matriz2,0,[])               
            else:
                print("Las matrices deben ser válidas")
        else:
            print("Las entradas que se ingresaron no son matrices")
    else:
        print("Las matrices no pueden estar vacías")

def sum_matRAux(matriz1,matriz2,i,res):
    if largoFilasR(matriz1) == i:
        return res
    else:
        return sum_matRAux(matriz1,matriz2,i+1,res+[sumFilasR(matriz1[i],matriz2[i])])
    
def validaR(matriz1,matriz2):
    if largoFilasR(matriz1) == largoFilasR(matriz2) and largoColumnasR(matriz1) == largoColumnasR(matriz2):
        return True
    else:
        return False    

def largoListaR(lista):
    if lista == []:
        return 0
    else:
        return 1 + largoListaR(lista[1:])

def sumFilasR(fila1,fila2):
    return sumFilasRAux(fila1,fila2,[])

def sumFilasRAux(fila1,fila2,res):
    if fila1 == []  and fila2 == []:
        return res
    else:
        return sumFilasRAux(fila1[1:],fila2[1:],res+[fila1[0]+fila2[0]])


##4
#E: Dos matrices
#S: La multiplicación de ambas matrices
#R: Los elementos de las matrices deben ser números. Las matrices deben ser válidas.


    
