def contador(lista):
        res=[0,0,0]
        while lista!=[]:
            if isinstance(lista[0],int):
                if lista[0]==0:
                    res[1]+=1
                elif lista[0]>0:
                    res[2]+=1
                else:
                    res[0]+=1
                lista=lista[1:]
            else:
                print("Las entradas deben ser números enteros")
        return res

def largo(lista):
    res=0
    while lista!=[]:
        res+=1
        lista=lista[1:]
    return res
        
def intercalar(lista1,lista2):
    if largo(lista1) == largo(lista2):
        res=[]
        while lista1!=[]:
                res+=[lista1[0]]
                res+=[lista2[0]]
                lista1=lista1[1:]
                lista2=lista2[1:]
        return res
    else:
        print("Las listas deben ser del mismo tamaño")
def aparece(dig,lista):
    while lista!=[]:
        if lista[0]==dig:
            return True
        lista=lista[1:]
    return False

def interseccion(lista1,lista2):
    if largo(lista1) == largo(lista2):
        if lista1!=[] or lista2!=[]:
            res=[]
            while lista1!=[]:
                if aparece(lista1[0],lista2):
                    res+=[lista1[0]]
                    lista1=lista1[1:]
            return res
        else:
            print("Las listas no pueden ser vacías")
    else:
        print("Las listas deben ser del mismo tamaño")

    
