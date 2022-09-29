#E: un número.
#S: Verificar si el número es primo mediante un valor booleano.
#R:El número tiene que ser entero y positivo.
def primos(n):
    if isinstance(n,int):
        if (n==0 or n==1):
            return False
        else:
            return primos_aux(n,2)
    else:
        print("Error")
        
def primos_aux(n,div):
    if (n==div):
        return True
    elif(n%2==0):
        return False
    else:
        if (n%div==0):
            return False
        elif (div==2):
            return primos_aux(n,div+1)
        else:
            return primos_aux(n,div+2)
