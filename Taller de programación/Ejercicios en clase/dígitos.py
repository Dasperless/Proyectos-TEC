# /Ejercicios 1/
#E:Un numero.
#S:La cantidad de digitos.
#R:Tiene que ser un número entero positivo.
def digitos(num):
    if isinstance (num, int) and num >= 0:
        if num ==0:
            return 0
        else:
            return 1+digitos(num//10)
    else:
        print ("el número tiene que ser un número entero positivo")
#/Ejercicio 2/
#E:Un número 
#S:Sumar los digitos
#R:El número tiene que ser un entero positivo
def suma_digitos(num):
    if isinstance (num, int) and num >= 0:
        if num ==0:
            return 0
        else:
            return num%10+suma_digitos(num//10)
    else:
        print ("el número tiene que ser un número entero positivo")
#/Ejercicio 3/
#E:Un número 
#S:Multiplicar los dígitos
#R:El número tiene que ser un entero positivo
def mult_digitos(num):
    if isinstance (num, int) and num >= 0:
        if num <10:
            return num
        else:
            return mult_digitos_aux(num)
    else:
        print ("el número tiene que ser un número entero positivo")
def mult_digitos_aux(num):
    if num==0:
        return 1
    else:
        return (num%10)*mult_digitos(num//10)
        
#/Ejercicio 4/
#E:Un número 
#S:Ascendente los dígitos
#R:El número tiene que ser un entero positivo
def ascendente(num):
    if isinstance(num,int) and num >=0:
        if num<10:
            return True
        else:
            return ascendente_aux(num)
    else:
        print("El número tiene que ser entero y positivo")
                
def ascendente_aux(num):
    if (num==0):
        return True
    else:
        if ((num//10)%10)<=(num%10):
            return ascendente_aux(num//10)
        else:
            return False        
    
#/Ejercicio 5/
#E:Un número 
#S:Verificar si un dígito es igual a cero
#R:El número tiene que ser un entero positivo
