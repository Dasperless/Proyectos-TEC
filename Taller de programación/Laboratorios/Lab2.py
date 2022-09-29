#E:Un número (n)
#S:Un número formado por los dígitos impares de n
#R:El número debe ser entero positivo
def verif_impares(n):
    if n%2!=0:
        return True
    else:
        return False
def impares(n):
    if isinstance(n,int):
        if n >=0:
            res=0
            exp=0
            while n!=0:
                if verif_impares(n%10):
                    res+= (n%10)*10**exp
                    exp+=1
                n//=10
            return res
        else:
            print("El número no es positivo")
    else:
        print("El número no es entero")

#E:Dos números (a y b)
#S:Si la suma de los digitos de la misma posición de a y b son primos debe retornar el nuevo número con los dígitos cambiados
#R:El número debe ser entero positivo y de la misma longitud
def primo(num):
    div=1
    divisores=0
    while div<=num:
        if (num%div)==0:
            divisores+=1
        div+=1
    if divisores==2:
        return True
    else:
        return False
def largo(num):
    res=0
    while num!=0:
        res+=1
        num//=10
    return res

def intercambiar(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if largo(a) == largo(b):
            res=0
            exp=0
            while a!=0:
                if primo((a%10)+(b%10)):
                    res+=(b%10)*10**exp
                else:
                    res+=(a%10)*10**exp
                a//=10
                b//=10
                exp+=1
                
            return res            
                    
        else:
            print("'a' ó 'b' no son del mismo largo")
    else:
        print(" 'a' ó 'b' no son enteros")
        
#E:Un número
#S:Imprime en la pantalla la conjetura de la sucesión de la conjetura Ulam
#R:El número debe ser entero positivo
def par(num):
    if num%2==0:
        return True
    else:
        return False
    
def ulam(num):
    if num>=0:
        if isinstance(num,int):
            while num!=1:
                print(num)
                if par(num):
                    num//=2
                else:
                    num=(num*3)+1
            print(num)                                  
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")
        
#E:Un número n y un dígito d
#S:Un número formado por los dígitos de n que son múltiplos de d
#R:El número debe ser entero positivo
def multiplos(n,d):
    if n>=0:
        if isinstance(n,int) and isinstance(d,int):
            if d>0 and d<9:
                res=0
                exp=0
                while n!=0:
                    if (n%10)%d == 0:
                        res+=(n%10)*10**exp
                        exp+=1
                    n//=10
                return res
            else:
                print("'d' no es un dígito")
                    
        else:
            print("'n' ó 'd' no es un número entero")
    else:
        print("El número no es positivo")
    
