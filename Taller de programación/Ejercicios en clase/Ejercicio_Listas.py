#E: Un número
#S: La sumatoria del numero desde 0
#R: El número tiene que ser entero y positivo.

def sumatoria(n):
    if isinstance(n,i) and n>0:
        return sumatoria_aux(n,0)
    else:
        print ("Error..")
def sumatoria_aux(n,sum):
    if n==0:
        return sum
    else:
        return sumatoria_aux(n-1,sum+n)

#E: Una lista con números
#S: La multiplicación de los números
#R: El número tiene que ser entero.

def multi(lista):
    if isinstance(lista,list) and lista != []:
        return multi_aux(lista,1)
    else:
        print ("La lista debe ser un número entero o flotante")

def multi_aux(lista, l_res):
    if lista==[]:
        return l_res
    else:
        return multi_aux(lista[1:],lista[0]*l_res)
    
#E: Una lista con números
#S: Unir a los pares
#R: Los números tienen que ponerse en una lista
def unir_pares(lista):
    if isinstance(lista,list) and lista != []:
        return unir_pares(lista,0) 
    else:
        print ("Error, la variable tiene que ser una lista con numeros y no puede esta vacia")
#def unir_pares_aux

#Ascendente(5)
#[1,2,3,4,5]

#Sum([4,1,3]),[6,2,3])
#[10,3,6]
