

#E: Una matriz.
#S: Verificar mediante un valor booleano si la matriz es identidad o no.
#R: La matriz tiene que ser válida y cuadrada.
def I_matriz(A):
    if comprobar(A):
        if len(A)==len(A[0]):
        else:
            print("La matriz tiene que ser cuadrada")
    else:
        print("La matriz tiene que ser válida")
        
#Comprobar que la matriz sea válida
def comprobar(A):
    return comprobar_aux(A,len(A)-1)
def comprobar_aux(A,i):
    if i==0:
        return True
    elif len(A[i-1])==0 and len (A[i])==len(A[i]):
        return True
    elif len(A[i])==len(A[i-1]):
        return comprobar_aux(A,i-1)
    else:
        return False

#Comprobar que lo que se encuentra dentro de la matríz sea un entero
def entero(A):
    return entero_aux(A,0,len(A),0,len(A[0])
def entero_aux(A,i,n,j,m):
    if i==n:
        return True
    elif isinstance(m[i][j],int)
          return entero_aux(A,i+1mlen)
#comprobar si en los pares ordenados iguales es 1
def 
