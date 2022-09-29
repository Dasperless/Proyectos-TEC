#E:Un número
#S:La cantidad de dígitos
#R:El número debe ser entero y positivo
def cantidad_digitos(num):
    if isinstance(num,int):
        if num>=0:
            res=0
            while num!=0:
                res+=1
                num//=10
            return res
        else:
            print("El número no es positivo")
    else:
        print("El número no es entero")

#E:Un número
#S:La cantidad de dígitos pares
#R:El número debe ser entero y positivo
def digitos_pares(num):
    if num>=0:
        if isinstance(num,int):
            res=0
            while num != 0:
                if (num%10)%2==0:
                    res+=1
                num//=10
            return res
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")

#E:Un número
#S:La cantidad de dígitos primos
#R:El número debe ser entero y positivo
def digitos_primos(num):
    if num>=0:
        if isinstance(num,int):
            res=0
            while num != 0:
                if primos(num%10):
                    res+=1
                num//=10
            return res
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")
        
def primos(num):
    if num>=2:
        div=2
        while div<num:
            if num%div==0:
                return False
            div+=1
        return True
    else:
        return False

#E:Un número
#S:El número invertido
#R:El número debe ser entero y positivo
def invertir(num):
    if num>=0:
        if isinstance(num,int):
            exp=largo(num)-1
            res=0
            while num!=0:
                res+=(num%10)*10**exp
                exp-=1
                num//=10
            return res
                
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")

def largo(num):
    res=0
    while num!=0:
        res+=1
        num//=10
    return res

#E:Un número
#S:Formar número con pares
#R:El número debe ser entero y positivo
def numero_pares(num):
    if num>=0:
        if isinstance(num,int):
            exp=0
            res=0
            while num!=0:
                if (num%10)%2==0:
                    res+=(num%10)*10**exp
                    exp+=1
                num//=10
            return res
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")
        
#E:Un número
#S:Sumar un número a todos los dígitos
#R:El número debe ser entero y positivo
def sumax(num,x):
    if num>=0:
        if isinstance(num,int):
            if x>=0 and x<=9:
                exp=0
                res=0
                while num!=0:
                    if largo(num%10+x)==1:
                        res+=(num%10+x)*10**exp
                        exp+=1
                        num//=10
                    else:
                        res+=(num%10+x)*10**exp
                        exp+=2
                        num//=10                        
                        
                return res
            else:
                print("x no es un digito")
            
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")
        
#E:Un número
#S:Sumar los dígitos de un número
#R:El número debe ser entero y positivo
def suma_digitos(num):
    if num>=0:
        if isinstance(num,int):
            res=0
            while num!=0:
                res+=(num%10)
                num//=10
            return res
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")
        
#E:Un número
#S:Hacer la secuencia de fibonacci
#R:El número debe ser entero y positivo
def fibonacci(num):
    if num>=0:
        if isinstance(num,int):
            fib=0
            res=0
            ant=0
            transant=0
            while fib!=num:
                res+=ant+transant
                ant=res-1
                fib+=1
                transant=fib-2
                print(ant,"anterior")
                print(transant,"transanterior")
            return res
        else:
            print("El número no es entero")
    else:
        print("El número no es positivo")

def prueba(num):
    while num!=0:
        ant=num%10
        print(ant)
        num//=10
    return True
