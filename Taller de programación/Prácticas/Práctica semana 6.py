#contador(475263)
#>>>312

#Union_asc(42619,253)
#>>>12234569

def largo(num):
    res=0
    while num!=0:
        res+=1
        num//=10
    return res

def mayor(num,dig):
    while num!=0:
        if num%10>dig:
            return False
        num//=10
    return True
    
def ascendente(num):
    res=0
    cont=0
    l=largo(num)-1
    while num!=0:
        if mayor(num//10,num%10):
            res+=num%10*10**cont
            cont+=1
            num//=10
        else:
            num=(num//10)+(num%10)*10**l
            l-=1
    return res
    
def Union_asc(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        if num1>0 and num2>0:
            if largo(num1)>largo(num2):
                suma=num1*10**(largo(num2))+num2
                return ascendente(suma)
            else:
                suma=num2*10**(largo(num1))+num1
                return ascendente(suma)
        else:
            print("los números deben ser positivos")
    else:
        print("Los números deben ser enteros")
