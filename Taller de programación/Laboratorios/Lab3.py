#E: Una lista (lista) y un número entero(n)
#S: Una nueva lista con dos elementos: la suma desde 0 hasta indice-1, y la suma de todos los números de la lista con idices desde ídice hasta al final de la lista.
#R: La lista no debe estar vacia, la lista debe contener números.

def largo(lista):
    res=0
    while lista!=[]:
        res+=1
        lista=lista[1:]
    return res

def suma_elementos(lista,n):
    if lista != []:
        if isinstance(lista,list):
            if isinstance(n,int):
                if n<largo(lista):
                    res=[0,0]
                    suma1=0
                    suma2=0
                    indice=0
                    while lista!=[]:
                        if isinstance(lista[0],int):
                            if indice<n:
                                suma1+=lista[0]
                                lista=lista[1:]
                                indice+=1
                            else:
                                suma2+=lista[0]
                                lista=lista[1:]
                        else:
                            print("La lista no contiene solo números enteros")
                    res[0]=suma1
                    res[1]=suma2
                    return res                    
                    return res
                else:
                    print("n no puede ser mayor que el largo de la lista ")
            else:
                print("n no es un número entero")
        else:
            print("lista no es una lista")
    else:
        print("La lista no puede estar vacía")

#E: Dos listas (lista1y lista2)
#S: una lista con los elementos de la lista1 que no estan en la lista2
#R: Las listas no pueden estar vacías
def no_existe(e,lista):
    while lista!=[]:
        if e==lista[0]:
            return False
        lista=lista[1:]
    return True
        
def exclusion(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):
        if lista1!=[] and lista2!=[]:
            res=[]
            while lista1!=[]:
                if no_existe(lista1[0],lista2):
                    res=res+[lista1[0]]
                lista1=lista1[1:]
            return res            
        else:
            print("Las listas no pueden estar vacías")
    else:
        print("Lista1 y lista2 deben ser listas")

#E:Una lista(lista)
#S:Una lista que indique en cada una de las posiciones la cantidad de veces que apareción ese dígito(el que indica la posición)
#R:La lista no puede estar vacía. la lista debe contenener valores entre 0 y n-1. Los elementos de la lista deben ser números
def frecuencia_d(d,lista):
    res=0
    while lista!=[]:
        if d==lista[0]:
            res+=1
        lista=lista[1:]
    return res
        
def frecuencias(lista):
    if isinstance(lista,list):
        if lista!=[]:
            i=0
            res=[]
            while i<largo(lista):
                if isinstance(lista[i],int):
                    res=res+[frecuencia_d(i,lista)]
                    i+=1
                else:
                    print("La lista debe contener número")
            return res           
        else:
            print("La lista no puede estar vacia")
    else:
        print("lista debe ser una lista")

#E:Una lista(lista)
#S:Verificar mediante un valor booleano si la lista es palindroma (True si es palindroma y False si no es palindroma)
#R: La lista no puede estar vacía. Los elementos de la lista deben ser números
def lista_palindroma(lista):
    if isinstance(lista,list):
        if lista!=[]:
            i=0
            j=-1
            while i<(largo(lista)//2):
                if lista[i]!=lista[j]:
                    return False
                i+=1
                j-=1
            return True       
        else:
            print("La lista no puede estar vacia")
    else:
        print("lista debe ser una lista")
