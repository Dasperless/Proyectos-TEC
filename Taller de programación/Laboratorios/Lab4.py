#----------------------------------------Bubble sort
#E: Una lista.
#S: La lista ordenada ascendentemente
#R: lista debe ser una lista con números enteros.
def burbuja(lista):
    if not isinstance(lista,list):
        return "Lista debe ser una lista"
    elif lista == []:
        return "La lista esta vacía"
    else:
        return burbuja_aux(lista,0)
    
def burbuja_aux(lista,i):
    if menor(lista):
        if i < len(lista)-1:
            if lista[i]> lista[i+1]:
                temp = lista[i]
                lista[i] =lista[i+1]
                lista[i+1]=temp
                swap=True
                return burbuja_aux(lista,i+1)
            else:
                return burbuja_aux(lista,i+1)
        else:
            return burbuja_aux(lista,0)
        
    else:
        return lista

def menor(lista):
    if len(lista) == 1 or lista == []:
        return False
    elif lista[0]< lista[1]:
        return menor(lista[1:])
    else:
        return True
#-------------------------------Selection sort
#E: Una lista.
#S: La lista ordenada ascendentemente.
#R: lista debe ser una lista con números enteros.
def seleccion(lista):
    if not isinstance(lista,list):
        return "Lista debe ser una lista"
    elif lista == []:
        return "La lista esta vacía"
    else:
        return seleccion_aux(lista,0)

def seleccion_aux(lista,cont):
    if cont >=len(lista):
        return lista
    else:
        m = cont+pos_menor(lista[cont:])
        temp = lista[m]
        lista[m] = lista[cont]
        lista[cont] = temp
        return seleccion_aux(lista,cont+1)
    
def pos_menor(lista):
    return pos_menor_aux(lista,0,0)

def pos_menor_aux(lista,m,cont):
    if cont >len(lista)-1:
        return m
    elif menor_lista(lista,lista[cont]):
        return pos_menor_aux(lista,cont,cont+1)
    else:
        return pos_menor_aux(lista,m,cont+1)
    
def menor_lista(lista,n):
    if lista == []:
        return True
    elif n <= lista[0]:
        return menor_lista(lista[1:],n)
    else:
        return False
    
#------------------ Insert sort
#E: Una lista.
#S: La lista ordenada ascendentemente.
#R: lista debe ser una lista con números enteros.
def insercion(lista):
    if not isinstance(lista,list):
        return "Lista debe ser una lista"
    elif lista == []:
        return "La lista esta vacía"
    else:
        return insercion_aux(lista)
def insercion_aux(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        piv = lista[0]
        menores = insercion_aux(lista_menores(lista,piv))
        mayores = insercion_aux(lista_mayores(lista,piv))
        
        return menores+[piv]+mayores
    
def lista_mayores(lista,piv):
    if lista == []:
        return []
    else:
        if lista[0]>piv:
            return [lista[0]]+lista_mayores(lista[1:],piv)
        else:
            return lista_mayores(lista[1:],piv)
        
def lista_menores(lista,piv):
    if lista == []:
        return []
    else:
        if lista[0]<piv:
            return [lista[0]]+lista_menores(lista[1:],piv)
        else:
            return lista_menores(lista[1:],piv)    
