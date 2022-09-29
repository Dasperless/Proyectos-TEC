def largo(num):
    res=0
    while num!=0:
        res+=1
        num//=10
    return res
def invertir(num):
    res=0
    exp=largo(num)-1
    while num>0:
        res+=(num%10)*10**exp
        num//=10
        exp-=1
    return res
def saltos(num):
    if num>0 and isinstance(num,int):
        res=0
        cont=0
        inv=invertir(num)
        while inv!=0:
            res+=(inv%10)*10**cont
            inv//=100
            cont+=1
        return invertir(res)
    else:
        print("El  número es  debe ser entero y positivo")
