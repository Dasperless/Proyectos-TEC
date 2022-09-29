#E: La medida de 4 lados
#S: El perímetro si es un cuadrado, el área si no lo es
#R: Los lados tienen que ser números entero y positivos

def lados(lado1,lado2,lado3,lado4):
    if isinstance(lado1,int) and isinstance(lado2,int) and isinstance(lado3,int) and isinstance(lado4,int):
        #Cuadrado
        if lado1>0 and lado2>0 and lado3>0 and lado4>0:
            if lado1 == lado2 and lado1 == lado3 and lado1== lado4:
                perimetro=lado1+lado2+lado3+lado4
                return perimetro
        #Rectángulo
            if lado1>lado2:
                area=lado1*lado2
                return area
            elif lado2>lado1:
                area=lado2*lado1
                return area
            elif lado2>lado3:
                area=lado2*lado3
                return area                
            elif lado3>lado2:
                area=lado3*lado2
                return area                
            elif lado3>lado4:
                area=lado3*lado4
                return area                
            elif lado4>lado3:
                area=lado4*lado3
                return area            
        else:
            print("Alguno de los lados no es positivo")
    else:
        print("Alguno de los lados no es un entero")
        
#E: Un número
#S: La suma de los dígitos
#R: El número tiene que ser entero, de tres dígitos y positivo

def suma_digitos(numero):
    if isinstance(numero,int):
        if numero>=100:
            digito1=numero%10
            digito2=(numero//10)%10
            digito3=numero//100
            resultado=digito1+digito2+digito3
            return resultado
        else:
            print("El número no es de 3 dígitos")
        
    else:
        print("El número no es entero")

#E: Ninguna
#S: La suma de los dígitos
#R: Los números tienen que ser enteros y positivos
def calculadora():
    num1 = int(input("Número 1 "))
    num2 = int(input("Número 2 "))
    print("1)Suma","2)Resta","3)Multiplicación","4)División")
    operacion=int(input("Elija la operación "))
    if operacion == 1:
        return num1+num2
    elif operacion == 2:
        return num1-num2
    elif operacion == 3:
        return num1*num2
    elif operacion == 4:
        return num1/num2
    
