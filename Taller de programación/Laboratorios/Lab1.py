#E: Un dígito(dig) y un número(num).
#S: Retornar el número truncado
#R num debe ser un número de cuatro dígitos entero y dig un dígito entre 1 y 9.

def truncado(dig,num):
    if num>=1000 and  num<=9999 and isinstance(num,int):
        if dig >=1 and dig <=9 and isinstance(dig,int):
            cont=0
            res=0
            while num!=0:
                res+=(num%10//dig)*10**cont
                cont+=1
                num//=10
            return res
        else:
            print("dig debe ser un dígitos entero entre 1 y 9")
    else:
        print("num debe ser un número entero de 4 dígitos")

#E: Un número
#S: Determinar si todos los dígitos del número son impares mediante un valor booleano(True si todo son impares, False si hay un digito par)
#R El número debe ser de 3 dígitos y entero
def  impares(num):
    if num >= 100 and num <= 999:
        if isinstance(num,int):
            while num!=0:
                if (num%10)%2==0:
                    return False
                num//=10            
            return True
        else:
            print("num debe ser un número entero")
    else:
        print("num debe ser de 3 dígitos")
        
#E: Un número
#S: Determinar si el número es palindromo (True si el número es palíndromo y False si no lo es) 
#R El número debe ser de 5 dígitos y entero
def palindromo(num):
    if num >=10000 and num<=99999:
        if isinstance(num,int):
            cont=4
            n=num
            pal=0
            while n!=0:
                pal+=(n%10)*10**cont
                n//=10
                cont-=1
            if num==pal:
                return True
            else:
                return False
        else:
            print("num debe ser un número entero")
    else:
        print("num debe ser un número de 5 dígitos")

#E: El destino o actividad 
#S: El destino y la actividad
#R Las personas con problemas cardiacos no pueden realizar bungee
def  viaje():
    print("¿Cuál actividad desea realizar?")
    lugar=input("1)Playa  2) Montaña\n\n")
    if lugar == "1":
        print("¿Desea viajar al Caribe o al Pacifico?")
        mar=input(" 1) Caribe  2) Pacifico \n\n")
        if mar=="1":
            print("¿Qué tipo de actividad desea realizar?")
            actividad=input("1)Surf  2)Fútbol playa \n\n")
            if actividad == "1":
                print("Buscando lugares de Caribe con Surf")
            elif  actividad == "2":
                print("Buscando lugares de Caribe con fútbol playa")
            else:
                print("Esa opción no existe")
        elif mar=="2":
            print("¿Qué tipo de actividad desea realizar?")
            actividad=input("1)Surf  2)Fútbol playa \n\n")
            if  actividad == "1":
                print("Buscando lugares de Pacífico con Surf")
            elif actividad == "2":
                print("Buscando lugares de Pacífico con fútbol playa")
            else:
                print("Esa opción no existe")
    elif lugar=="2":
        actividad=input("1)Canopy  2)Bongee   3)Aguas termales\n\n")
        if actividad=="1":
            print("Buscando lugares de montaña con Canopy")           
        elif actividad=="2":
            print("¿Tiene problemas cardiacos?")
            problemas_cardiacos=input("1)Sí  2)No\n\n")
            if problemas_cardiacos=="1":
                print("No puedes realizar bongee")
            elif problemas_cardiacos=="2":
                print("Buscando lugares de montaña con Bongee")  
        elif actividad=="3":
            print("Buscando lugares de montaña con aguas termales") 

                
        else:
            print("Esa opción no existe")
    else:
        print("Esa opción no existe")
        
    

#E: Un número
#S: retorna la suma de los dígitos pares
#R El número debe ser de 3 dígitos y entero
def pares(num):
    if isinstance(num,int):
        if num>=100 and num<=999:
            res=0
            while num!=0:
                if (num%10) %2==0:
                    res+=num%10
                    num//=10
                else:
                    num//=10           
            return res
        else:
            print("El número debe ser de 3 dígitos")
    else:
        print("Sólo se aceptan números enteros")
