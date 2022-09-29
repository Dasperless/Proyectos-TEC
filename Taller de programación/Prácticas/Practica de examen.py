#1
#suma elementos
def validaciones(lista):
    if isinstance(lista,list):
        while lista!=[]:
            if isinstance(lista[0],int):
                lista=lista[1:]
            else:
                return False
        return True
    else:
        return False
def largo(lista):
    res=0
    while lista!=[]:
        res+=1
        lista=lista[1:]
    return res

def suma_elementos(lista,indice):
    if validaciones(lista):
        if isinstance(indice,int):
            if largo(lista)>=indice:
                res=[]
                sum1=0
                sum2=0
                for i in lista[:indice]:
                    sum1+=i
                for j in lista[:-1]:
                    sum2+=i
                res+=[sum1,sum2]
                return res
            else:
                print("El índice está fuera del rango")
        else:
            print("El indice debe ser un número entero")
    else:
        print("la lista debe ser una lista con elementos númericos enteros")

def menor(lista,n):
    while lista!=[]:
        if n<=lista[0]:
            lista=lista[1:]
        else:
            return False
    return True

def ordenar(lista):
    res=[]
    while lista!=[]:
        if menor(lista[1:],lista[0]):
            res+=[lista[0]]
        else:
            lista+=[lista[0]]
        lista=lista[1:]
    return res

def merge(lista1,lista2):
    if validaciones(lista1) and validaciones(lista2):
        res=lista1+lista2
        return ordenar(res)
    else:
        print("La lista debe ser una lista con elementos numéricos")

def natural(lista):
    if validaciones(lista):
        return naturalAux(lista,0,0)
    else:
     print("La lista debe ser una lista con elementos numéricos")
def naturalAux(lista,res,suma):
    if lista==[]:
        if suma!=[]
            return res
        else:
            retur
    elif menor(lista[1:],lista[0]):
        
        
