"""
|---------Reloj----------|
|       #minutos         |
|        #Horas          |
|------------------------|
|+ AvanzarM()            |
|+ AvanzarH()            |
|+ MostrarH()            |
|    "la hora es: 4:10"  | 
|+ SetearH(h,m)          |
|------------------------|
"""

class reloj:
    def __init__(self,h,m):
        self.h=h
        self.m=m
        
    def AvanzarM(self):
        if self.m != 59:
            self.m += 1
        else:
            self.h += 1
            self.m = 00
            
    def AvanzarH(self):
        if self.h == 24:
            self.h=0
        else:
            self.h+=1
        
    def MostrarH(self):
        if self.m == 0 and self.h == 0:
            print("La hora es ",self.h,self.h,":",self.m,self.m)
        elif self.h == 0:
            print("La hora es ",self.h,self.h,":",self.m)
        elif self.m ==0:
            print("La hora es ",self.h,":",self.m,self.m)           
        else:
            print("La hora es ",self.h,":",self.m)
        
    def SetearH(self,h,m):
        if h>=0 and h <=24 and m>=0 and m<=59:
            self.h=h
            self.m=m
        else:
            print("No se puede setear esa hora")
        
        
