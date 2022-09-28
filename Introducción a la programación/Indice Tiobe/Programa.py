
from tabulate import tabulate
#E: No tiene entradas
#S: La opción ingresada
#R: El input debe ser un string
def obtenerOpcion():
    menu ="""
    1) Top de lenguajes de programación
    2) Cantidad de lenguajes por paradigma
    3) Detalles de lenguaje por nombre
    4) Salir
    """
    print (menu)
    return input("Seleccione una opción: ")

#E: una matriz de 4xn y el nombre
#S: Una lista con los detalles del lenguaje por nombre
#R: La tabla debe ser una matris 4xn y nombre un string
def obtenerPorNombre(tabla,nombre):
    if len(tabla) == 0:
        return []
    if tabla[0][1] == nombre:
        return tabla[0] + obtenerPorNombre(tabla[1:],nombre)
    return obtenerPorNombre(tabla[1:],nombre)

#E: El contenido y el inicio y el fin que es el indice de filas a retornar
#S: Una matriz con las filas de las tablas
#R: Contenido es una matriz, inicio y fin son números.
def obtenerFilas(contenido,inicio,fin):
    return contenido.split("\n")[inicio:fin]

#E: El contenido
#S: Obtiene el encabezado del contenido
#R: El contenido debe ser un string
def obtenerEncabezado(contenido):
    return obtenerColumnas(obtenerFilas(contenido,0,1))[0]

#E: Un string
#S: La representacion de un csv en una matriz
#R: Contenido es un string
def convertirMatriz(contenido):
    filas = obtenerFilas(contenido,0,len(contenido))
    return obtenerColumnas(filas)

#E: Una lista de strings que representa las filas de la tabla
#S: Una matriz con las filas y columnas del contenido
#R: filas debe ser una lista con strings con comas
def obtenerColumnas(filas):
    if(len(filas) == 0):
        return []
    return [filas[0].split(",")] + obtenerColumnas(filas[1:])

#E: Contenido que es una matriz y paradigma que es un string
#S: Un número con la cantidad de lenguajes que son del paradigma ingresado
#R: contenido debe ser una matriz y paradigma un string
def contarPorParadigma(contenido,paradigma):
    if(len(contenido) == 0):
        return 0
    elif(contenido[0][2] == paradigma):
        return 1 + contarPorParadigma(contenido[1:], paradigma)
    else:
        return contarPorParadigma(contenido[1:], paradigma)

    
def inicio():
    op = obtenerOpcion()

    if op=="1":
        print(tabulate(sorted(tabla), headers=encabezados))
        return inicio()

    elif op=="2":
        paradigma = input("Ingrese el paradigma: ")
        print("Cantidad: ", contarPorParadigma(tabla,paradigma))
        return inicio()

    elif op=="3":
        nombre = input("Ingrese el nombre: ")
        detallesXNombre = obtenerPorNombre(tabla,nombre)
        print(tabulate([detallesXNombre], headers=encabezados))
        return inicio()

    elif op=="4":
        exit()
    else:
        print ("""
        la opción es invalida
        """)
        return inicio()

abrir=open('indice\Tiobe_index.txt','r')
leer=abrir.read()
encabezados = obtenerEncabezado(leer)
tabla = convertirMatriz(leer)[1:]
inicio()
     
