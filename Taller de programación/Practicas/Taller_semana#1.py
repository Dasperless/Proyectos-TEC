#E:Perímetro y la apotema
#S:El área de la figura
#R:el perimetro y la apotema deben ser positivos 
def area_pentagono(perimetro,apotema):
    resultado=perimetro*apotema/2
    return resultado

#E:Base mayor,base menor y altura
#S:El área de un trapecio
#R:las bases y la altura tienen que ser positivas
def area_trapecio(base_mayor,base_menor,altura):
    resultado=base_mayor+base_menor/2*6
    return resultado

#E:radio
#S:El área de una esfera
#R:el radio debe ser positivo
def area_esfera(radio):
    resultado= 4*3.14*r**2
    return resultado

#E:radio
#S:El área de una esfera
#R:el radio debe ser positivo.
def area_elipse (semieje_mayor, semieje_menor):
    resultado= 3.14*semieje_mayor*semieje_menor
    return resultado

    
