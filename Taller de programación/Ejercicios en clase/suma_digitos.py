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
