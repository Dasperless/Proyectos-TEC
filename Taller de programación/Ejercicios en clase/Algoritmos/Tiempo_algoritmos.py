import random
try:
    import time
except ImportError:
    print("necesita instalar la librería")
    
#Algoritmo burbuja
def bubble_sort(lista):
    swap = True
    while swap:
        swap = False
        i = 0
        while i < len(lista)-1:
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                swap = True
            i +=1
        #print(lista)
    return lista


#Algoritmo Selección
def selection_sort(lista):
    for i in range(0, len(lista)):
        m = i+menor(lista[i:])
        temp = lista[m]
        lista[m] = lista[i]
        lista[i] = temp
        #print(i, m, lista, lista[i:])
    return lista

def menor(lista):
    m = 0
    for i in range(0, len(lista)):
        if lista[i] < lista[m]:
            m = i
    return m

#Algoritmo de inserción
def insertsort(lista):
    for i in range(1,len(lista)):
        pos = i
        while pos > 0 and lista[pos-1] > lista[i]:
            pos -= 1
        lista = lista[:pos] + [lista[i]] + lista[pos:i] + lista[i+1:]
    return lista

#Algoritmo Rápido
def qsaux(lista):
    if len(lista)==1 or len(lista)==0:
        return lista
    else:
        pivote = lista[-1]
        menores = [x for x in lista[:-1] if x < pivote]
        mayores = [x for x in lista[:-1] if x >= pivote]
        return qsaux(menores) + [pivote] + qsaux(mayores)

 #Números aleatorios
def listaAleatorios(n):
	lista = [0]  * n
	for i in range(n):
		lista[i] = random.randint(0, 1000)
	return lista
    
#medir bubble_sort
def medir_bubble_sort():
    l_aleatoria=listaAleatorios(1000)
    tiempo_inicial=time.time()
    bubble_sort(l_aleatoria)
    tiempofinal=time.time()-tiempo_inicial
    print("El algoritmo buble sort duró: ",tiempofinal,"Segundos")
    
#medir Selección
def medir_selection_sort():
    l_aleatoria=listaAleatorios(1000)
    tiempo_inicial=time.time()
    selection_sort(l_aleatoria)
    tiempofinal=time.time()-tiempo_inicial
    print("El algoritmo slection sort duró: ",tiempofinal,"Segundos")
    
#medir Insersión
def medir_insertsort():
    l_aleatoria=listaAleatorios(1000)
    tiempo_inicial=time.time()
    insertsort(l_aleatoria)
    tiempofinal=time.time()-tiempo_inicial
    print("El algoritmo insert sort duró: ",tiempofinal,"Segundos")

#medir qsaux
def medir_qsaux():
    l_aleatoria=listaAleatorios(1000)
    tiempo_inicial=time.time()
    qsaux(l_aleatoria)
    tiempofinal=time.time()-tiempo_inicial
    print("El algoritmo quick sort duró: ",tiempofinal,"Segundos")

  
