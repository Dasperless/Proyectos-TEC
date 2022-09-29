def enteros(matriz):
        for i in matriz:
                for j in i:
                        if isinstance(matriz[i][j],float) or isintance(matriz[i][j],str):
                                return False
        if isinstance(matriz[i][j],int):
                return True

def cuadrado(matriz):
        if len(matriz)== len (matriz[0]):
                return True
        else:
                return False

def valida(matriz):
        for i in range (0,len(matriz[0])):
                if len(matriz[i])!=len(matriz[0]):
                        print(len(matriz[i]))
                        return False
        return True
                

def sum_diagonal(M1,M2):
        if valida(M1) and valida(M2):
                if cuadrado (M1) and cuadrado(M2):
                        return sum_diagonal_aux(M1,M2,0,0,[])
                else:
                        print("La matriz debe ser cuadrada")
        else:
                print("Error, matrices incopatibles")

def sum_diagonal_aux(M1,M2,i,j,res):
        while i != len(M1):
                res+=[M1[i][j]+M2[i][j]]
                i+=1
                j+=1
        return res

#Anti primos 
def anti_primos(M):
        if valida(M):
                if cuadrado(M):
                        return anti_primos_aux(M,0,-1,0)
                else:
                        print("La matriz debe ser cuadarada")
        else:
                print("La matriz debe ser válida")
def primo(num):
        div=0
        for i in range(1,num+1):
                if num%i==0:
                        div+=1
        if div == 2:
                return True
        else:
                return False
def anti_primos_aux(M,i,j,res):
        while i != len(M):
                res+=M[i][j]
                i+=1
                j-=1
                
        if primo(res):
                return True
        else:
                return False
#Producto
def producto(V,M):
        if isinstance (V,list) and isinstance (M,list):
                if len(V) == len(M)-1:
                        if valida(M):
                                return producto_aux(V,M,len(M),res)
                        else:
                                print("La matriz debe ser válida")
                else:
                        print("El vector y la matriz deben tener la misma cantidad de valores")
        else:
                print("Las entradas deben ser un vector y una matriz")
